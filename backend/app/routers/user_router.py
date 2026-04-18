"""用户路由"""

from typing import Optional
from fastapi import APIRouter, Depends, Response, Query
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.user import (
    UserRegisterRequest, UserLoginRequest, UserAddRequest,
    UserUpdateRequest, UserVO, LoginUserVO, UserPageVO
)
from app.schemas.common import BaseResponse, PageRequest, DeleteRequest
from app.deps import get_session_id, get_current_user, require_login, require_admin
from app.services.user_service import user_service


def get_db():
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


user_router = APIRouter(prefix="/user", tags=["用户管理"])


@user_router.post("/register", summary="用户注册")
async def register(
        request: UserRegisterRequest,
        response: Response,
        db: Session = Depends(get_db)
) -> BaseResponse[UserVO]:
    """用户注册"""
    user, session_id = user_service.register(db, request)
    response.set_cookie(
        key="SESSION",
        value=session_id,
        httponly=True,
        max_age=2592000,
        samesite="lax"
    )
    return BaseResponse.success(
        data=UserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role,
            createTime=user.create_time,
            updateTime=user.update_time
        ),
        message="注册成功"
    )


@user_router.post("/login", summary="用户登录")
async def login(
        request: UserLoginRequest,
        response: Response,
        db: Session = Depends(get_db)
) -> BaseResponse[UserVO]:
    """用户登录"""
    user, session_id = user_service.login(db, request)
    response.set_cookie(
        key="SESSION",
        value=session_id,
        httponly=True,
        max_age=2592000,
        samesite="lax"
    )
    return BaseResponse.success(
        data=UserVO(
            id=user.id,
            userAccount=user.user_account,
            userName=user.user_name,
            userAvatar=user.user_avatar,
            userProfile=user.user_profile,
            userRole=user.user_role,
            createTime=user.create_time,
            updateTime=user.update_time
        ),
        message="登录成功"
    )


@user_router.post("/logout", summary="用户退出登录")
async def logout(
        response: Response,
        session_id: Optional[str] = Depends(get_session_id),
        current_user: LoginUserVO = Depends(require_login)
) -> BaseResponse[bool]:
    """用户退出登录"""
    if session_id:
        user_service.logout(session_id)
    response.delete_cookie(key="SESSION")
    return BaseResponse.success(data=True, message="退出成功")


@user_router.get("/current", summary="获取当前登录用户信息")
async def get_current(
        db: Session = Depends(get_db),
        current_user: LoginUserVO = Depends(require_login)
) -> BaseResponse[UserVO]:
    """获取当前登录用户信息"""
    user_vo = user_service.get_current_user(db, current_user.id)
    return BaseResponse.success(data=user_vo)


@user_router.get("/{id}", summary="根据ID获取用户信息（管理员）")
async def get_user_by_id(
        id: int,
        db: Session = Depends(get_db),
        current_user: LoginUserVO = Depends(require_admin)
) -> BaseResponse[UserVO]:
    """根据ID获取用户信息（管理员）"""
    user_vo = user_service.get_user_by_id(db, id)
    return BaseResponse.success(data=user_vo)


@user_router.get("/", summary="分页查询用户列表（管理员）")
async def list_users(
        current: int = Query(default=1, ge=1, description="当前页码"),
        page_size: int = Query(default=10, ge=1, le=100, alias="pageSize", description="每页大小"),
        query: Optional[str] = Query(default=None, description="搜索关键词"),
        db: Session = Depends(get_db),
        current_user: LoginUserVO = Depends(require_admin)
) -> BaseResponse[UserPageVO]:
    """分页查询用户列表（管理员）"""
    page_request = PageRequest(current=current, pageSize=page_size)
    result = user_service.list_users(db, page_request, query)
    return BaseResponse.success(data=result)


@user_router.post("/", summary="添加用户（管理员）")
async def add_user(
        request: UserAddRequest,
        db: Session = Depends(get_db),
        current_user: LoginUserVO = Depends(require_admin)
) -> BaseResponse[UserVO]:
    """添加用户（管理员）"""
    user_vo = user_service.add_user(db, request)
    return BaseResponse.success(data=user_vo, message="添加成功")


@user_router.put("/", summary="修改用户（管理员）")
async def update_user(
        request: UserUpdateRequest,
        db: Session = Depends(get_db),
        current_user: LoginUserVO = Depends(require_admin)
) -> BaseResponse[UserVO]:
    """修改用户（管理员）"""
    user_vo = user_service.update_user(db, request)
    return BaseResponse.success(data=user_vo, message="修改成功")


@user_router.delete("/", summary="删除用户（管理员）")
async def delete_user(
        request: DeleteRequest,
        db: Session = Depends(get_db),
        current_user: LoginUserVO = Depends(require_admin)
) -> BaseResponse[bool]:
    """删除用户（管理员）"""
    result = user_service.delete_user(db, request.id)
    return BaseResponse.success(data=result, message="删除成功")
