"""用户服务层"""

from datetime import datetime
from typing import Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.model.user import User
from app.schemas.user import (
    UserRegisterRequest, UserLoginRequest, UserAddRequest,
    UserUpdateRequest, UserVO, LoginUserVO, UserPageVO
)
from app.schemas.common import PageRequest
from app.exceptions import ErrorCode, BusinessException, throw_if, throw_if_not
from app.utils.password import encrypt_password, verify_password
from app.utils.session import session_store


class UserService:
    """用户服务"""

    @staticmethod
    def register(db: Session, request: UserRegisterRequest) -> Tuple[User, str]:
        """
        用户注册
        返回: (用户对象, session_id)
        """
        throw_if(
            request.user_password != request.check_password,
            ErrorCode.PARAMS_ERROR,
            "两次输入的密码不一致"
        )

        existing_user = db.query(User).filter(
            User.user_account == request.user_account,
            User.is_delete == 0
        ).first()
        throw_if(existing_user, ErrorCode.USER_ALREADY_EXIST, "账号已存在")

        encrypted_password = encrypt_password(request.user_password)

        user = User(
            user_account=request.user_account,
            user_password=encrypted_password,
            user_name=request.user_name or request.user_account,
            user_role="user"
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        login_user_vo = LoginUserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role
        )
        session_id = session_store.create_session(
            user_id=user.id,
            user_data=login_user_vo.model_dump()
        )

        return user, session_id

    @staticmethod
    def login(db: Session, request: UserLoginRequest) -> Tuple[User, str]:
        """
        用户登录
        返回: (用户对象, session_id)
        """
        user = db.query(User).filter(
            User.user_account == request.user_account,
            User.is_delete == 0
        ).first()
        throw_if_not(user, ErrorCode.USER_NOT_EXIST, "用户不存在")

        throw_if_not(
            verify_password(request.user_password, user.user_password),
            ErrorCode.PASSWORD_ERROR,
            "密码错误"
        )

        login_user_vo = LoginUserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role
        )
        session_id = session_store.create_session(
            user_id=user.id,
            user_data=login_user_vo.model_dump()
        )

        return user, session_id

    @staticmethod
    def logout(session_id: str) -> bool:
        """用户退出登录"""
        return session_store.delete_session(session_id)

    @staticmethod
    def get_current_user(db: Session, user_id: int) -> Optional[UserVO]:
        """获取当前登录用户信息"""
        user = db.query(User).filter(
            User.id == user_id,
            User.is_delete == 0
        ).first()
        throw_if_not(user, ErrorCode.USER_NOT_EXIST, "用户不存在")

        return UserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role,
            createTime=user.create_time,
            updateTime=user.update_time
        )

    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[UserVO]:
        """根据ID获取用户信息（管理员）"""
        user = db.query(User).filter(
            User.id == user_id,
            User.is_delete == 0
        ).first()
        throw_if_not(user, ErrorCode.USER_NOT_EXIST, "用户不存在")

        return UserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role,
            createTime=user.create_time,
            updateTime=user.update_time
        )

    @staticmethod
    def list_users(db: Session, page_request: PageRequest, query: Optional[str] = None) -> UserPageVO:
        """分页查询用户列表（管理员）"""
        query_builder = db.query(User).filter(User.is_delete == 0)

        if query:
            query_builder = query_builder.filter(
                or_(
                    User.user_account.like(f"%{query}%"),
                    User.user_name.like(f"%{query}%")
                )
            )

        total = query_builder.count()

        order_column = User.create_time
        if page_request.sort_order == "ascend":
            query_builder = query_builder.order_by(order_column.asc())
        else:
            query_builder = query_builder.order_by(order_column.desc())

        offset = (page_request.current - 1) * page_request.page_size
        users = query_builder.offset(offset).limit(page_request.page_size).all()

        records = [
            UserVO(
                id=user.id,
                userAccount=user.user_account,
                userName=user.user_name,
                userAvatar=user.user_avatar,
                userProfile=user.user_profile,
                userRole=user.user_role,
                createTime=user.create_time,
                updateTime=user.update_time
            )
            for user in users
        ]

        return UserPageVO(total=total, records=records)

    @staticmethod
    def add_user(db: Session, request: UserAddRequest) -> UserVO:
        """添加用户（管理员）"""
        existing_user = db.query(User).filter(
            User.user_account == request.user_account,
            User.is_delete == 0
        ).first()
        throw_if(existing_user, ErrorCode.USER_ALREADY_EXIST, "账号已存在")

        encrypted_password = encrypt_password(request.user_password)

        user = User(
            user_account=request.user_account,
            user_password=encrypted_password,
            user_name=request.user_name or request.user_account,
            user_avatar=request.user_avatar,
            user_profile=request.user_profile,
            user_role=request.user_role
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        return UserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role,
            createTime=user.create_time,
            updateTime=user.update_time
        )

    @staticmethod
    def update_user(db: Session, request: UserUpdateRequest) -> UserVO:
        """修改用户（管理员）"""
        user = db.query(User).filter(
            User.id == request.id,
            User.is_delete == 0
        ).first()
        throw_if_not(user, ErrorCode.USER_NOT_EXIST, "用户不存在")

        if request.user_name is not None:
            user.user_name = request.user_name
        if request.user_avatar is not None:
            user.user_avatar = request.user_avatar
        if request.user_profile is not None:
            user.user_profile = request.user_profile
        if request.user_role is not None:
            user.user_role = request.user_role
        if request.user_password is not None:
            user.user_password = encrypt_password(request.user_password)

        user.edit_time = datetime.now()
        db.commit()
        db.refresh(user)

        return UserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role,
            createTime=user.create_time,
            updateTime=user.update_time
        )

    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """删除用户（管理员）- 逻辑删除"""
        user = db.query(User).filter(
            User.id == user_id,
            User.is_delete == 0
        ).first()
        throw_if_not(user, ErrorCode.USER_NOT_EXIST, "用户不存在")

        user.is_delete = 1
        user.edit_time = datetime.now()
        db.commit()

        return True


user_service = UserService()
