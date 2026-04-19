declare namespace API {
  type addUserApiUserPostParams = {
    SESSION?: string | null;
  };

  type BaseResponseBool_ = {
    /** Code 状态码 */
    code?: number;
    /** Data 响应数据 */
    data?: boolean | null;
    /** Message 响应消息 */
    message?: string;
  };

  type BaseResponseUserPageVO_ = {
    /** Code 状态码 */
    code?: number;
    /** 响应数据 */
    data?: UserPageVO | null;
    /** Message 响应消息 */
    message?: string;
  };

  type BaseResponseUserVO_ = {
    /** Code 状态码 */
    code?: number;
    /** 响应数据 */
    data?: UserVO | null;
    /** Message 响应消息 */
    message?: string;
  };

  type DeleteRequest = {
    /** Id 要删除的 ID */
    id: number;
  };

  type deleteUserApiUserDeleteParams = {
    SESSION?: string | null;
  };

  type getCurrentApiUserCurrentGetParams = {
    SESSION?: string | null;
  };

  type getUserByIdApiUserIdGetParams = {
    id: number;
    SESSION?: string | null;
  };

  type HTTPValidationError = {
    /** Detail */
    detail?: ValidationError[];
  };

  type listUsersApiUserGetParams = {
    /** 当前页码 */
    current?: number;
    /** 每页大小 */
    pageSize?: number;
    /** 搜索关键词 */
    query?: string | null;
    SESSION?: string | null;
  };

  type logoutApiUserLogoutPostParams = {
    SESSION?: string | null;
  };

  type updateUserApiUserPutParams = {
    SESSION?: string | null;
  };

  type UserAddRequest = {
    /** Useraccount 账号 */
    userAccount: string;
    /** Userpassword 密码 */
    userPassword: string;
    /** Username 用户昵称 */
    userName?: string | null;
    /** Useravatar 用户头像 */
    userAvatar?: string | null;
    /** Userprofile 用户简介 */
    userProfile?: string | null;
    /** Userrole 用户角色 */
    userRole?: string;
  };

  type UserLoginRequest = {
    /** Useraccount 账号 */
    userAccount: string;
    /** Userpassword 密码 */
    userPassword: string;
  };

  type UserPageVO = {
    /** Total 总数 */
    total: number;
    /** Records 用户列表 */
    records?: UserVO[];
  };

  type UserRegisterRequest = {
    /** Useraccount 账号 */
    userAccount: string;
    /** Userpassword 密码 */
    userPassword: string;
    /** Checkpassword 确认密码 */
    checkPassword: string;
    /** Username 用户昵称 */
    userName?: string | null;
  };

  type UserUpdateRequest = {
    /** Id 用户ID */
    id: number;
    /** Username 用户昵称 */
    userName?: string | null;
    /** Useravatar 用户头像 */
    userAvatar?: string | null;
    /** Userprofile 用户简介 */
    userProfile?: string | null;
    /** Userrole 用户角色 */
    userRole?: string | null;
    /** Userpassword 密码 */
    userPassword?: string | null;
  };

  type UserVO = {
    /** Id 用户ID */
    id: number;
    /** Useraccount 账号 */
    userAccount: string;
    /** Username 用户昵称 */
    userName?: string | null;
    /** Useravatar 用户头像 */
    userAvatar?: string | null;
    /** Userprofile 用户简介 */
    userProfile?: string | null;
    /** Userrole 用户角色 */
    userRole: string;
    /** Createtime 创建时间 */
    createTime?: string | null;
    /** Updatetime 更新时间 */
    updateTime?: string | null;
  };

  type ValidationError = {
    /** Location */
    loc: (string | number)[];
    /** Message */
    msg: string;
    /** Error Type */
    type: string;
  };
}
