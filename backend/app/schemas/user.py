"""用户相关的请求和响应模型"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class UserRegisterRequest(BaseModel):
    """用户注册请求"""

    user_account: str = Field(..., alias="userAccount", min_length=4, max_length=256, description="账号")
    user_password: str = Field(..., alias="userPassword", min_length=8, max_length=512, description="密码")
    check_password: str = Field(..., alias="checkPassword", min_length=8, max_length=512, description="确认密码")
    user_name: Optional[str] = Field(None, alias="userName", max_length=256, description="用户昵称")

    class Config:
        populate_by_name = True


class UserLoginRequest(BaseModel):
    """用户登录请求"""

    user_account: str = Field(..., alias="userAccount", description="账号")
    user_password: str = Field(..., alias="userPassword", description="密码")

    class Config:
        populate_by_name = True


class UserAddRequest(BaseModel):
    """添加用户请求（管理员）"""

    user_account: str = Field(..., alias="userAccount", min_length=4, max_length=256, description="账号")
    user_password: str = Field(..., alias="userPassword", min_length=8, max_length=512, description="密码")
    user_name: Optional[str] = Field(None, alias="userName", max_length=256, description="用户昵称")
    user_avatar: Optional[str] = Field(None, alias="userAvatar", max_length=1024, description="用户头像")
    user_profile: Optional[str] = Field(None, alias="userProfile", max_length=512, description="用户简介")
    user_role: str = Field(default="user", alias="userRole", description="用户角色")

    class Config:
        populate_by_name = True


class UserUpdateRequest(BaseModel):
    """修改用户请求"""

    id: int = Field(..., description="用户ID")
    user_name: Optional[str] = Field(None, alias="userName", max_length=256, description="用户昵称")
    user_avatar: Optional[str] = Field(None, alias="userAvatar", max_length=1024, description="用户头像")
    user_profile: Optional[str] = Field(None, alias="userProfile", max_length=512, description="用户简介")
    user_role: Optional[str] = Field(None, alias="userRole", description="用户角色")
    user_password: Optional[str] = Field(None, alias="userPassword", min_length=8, max_length=512, description="密码")

    class Config:
        populate_by_name = True


class UserQueryRequest(BaseModel):
    """用户查询请求"""

    id: Optional[int] = Field(None, description="用户ID")
    user_account: Optional[str] = Field(None, alias="userAccount", description="账号")
    user_name: Optional[str] = Field(None, alias="userName", description="用户昵称")

    class Config:
        populate_by_name = True


class UserVO(BaseModel):
    """用户视图对象（响应）"""

    id: int = Field(..., description="用户ID")
    user_account: str = Field(..., alias="userAccount", description="账号")
    user_name: Optional[str] = Field(None, alias="userName", description="用户昵称")
    user_avatar: Optional[str] = Field(None, alias="userAvatar", description="用户头像")
    user_profile: Optional[str] = Field(None, alias="userProfile", description="用户简介")
    user_role: str = Field(..., alias="userRole", description="用户角色")
    create_time: Optional[datetime] = Field(None, alias="createTime", description="创建时间")
    update_time: Optional[datetime] = Field(None, alias="updateTime", description="更新时间")

    class Config:
        populate_by_name = True
        from_attributes = True


class LoginUserVO(BaseModel):
    """登录用户视图对象"""

    id: int = Field(..., description="用户ID")
    user_account: str = Field(..., alias="userAccount", description="账号")
    user_name: Optional[str] = Field(None, alias="userName", description="用户昵称")
    user_avatar: Optional[str] = Field(None, alias="userAvatar", description="用户头像")
    user_profile: Optional[str] = Field(None, alias="userProfile", description="用户简介")
    user_role: str = Field(..., alias="userRole", description="用户角色")

    class Config:
        populate_by_name = True


class UserPageVO(BaseModel):
    """用户分页响应"""

    total: int = Field(..., description="总数")
    records: List[UserVO] = Field(default_factory=list, description="用户列表")
