// @ts-ignore
/* eslint-disable */
import request from "@/request";

/** 分页查询用户列表（管理员） 分页查询用户列表（管理员） GET /api/user/ */
export async function listUsersApiUserGet(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.listUsersApiUserGetParams,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseUserPageVO_>("/api/user/", {
    method: "GET",
    params: {
      // current has a default value: 1
      current: "1",
      // pageSize has a default value: 10
      pageSize: "10",
      ...params,
    },
    ...(options || {}),
  });
}

/** 修改用户（管理员） 修改用户（管理员） PUT /api/user/ */
export async function updateUserApiUserPut(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.updateUserApiUserPutParams,
  body: API.UserUpdateRequest,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseUserVO_>("/api/user/", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    params: { ...params },
    data: body,
    ...(options || {}),
  });
}

/** 添加用户（管理员） 添加用户（管理员） POST /api/user/ */
export async function addUserApiUserPost(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.addUserApiUserPostParams,
  body: API.UserAddRequest,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseUserVO_>("/api/user/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    params: { ...params },
    data: body,
    ...(options || {}),
  });
}

/** 删除用户（管理员） 删除用户（管理员） DELETE /api/user/ */
export async function deleteUserApiUserDelete(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.deleteUserApiUserDeleteParams,
  body: API.DeleteRequest,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseBool_>("/api/user/", {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    params: { ...params },
    data: body,
    ...(options || {}),
  });
}

/** 根据ID获取用户信息（管理员） 根据ID获取用户信息（管理员） GET /api/user/${param0} */
export async function getUserByIdApiUserIdGet(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.getUserByIdApiUserIdGetParams,
  options?: { [key: string]: any }
) {
  const { id: param0, ...queryParams } = params;
  return request<API.BaseResponseUserVO_>(`/api/user/${param0}`, {
    method: "GET",
    params: { ...queryParams },
    ...(options || {}),
  });
}

/** 获取当前登录用户信息 获取当前登录用户信息 GET /api/user/current */
export async function getCurrentApiUserCurrentGet(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.getCurrentApiUserCurrentGetParams,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseUserVO_>("/api/user/current", {
    method: "GET",
    params: { ...params },
    ...(options || {}),
  });
}

/** 用户登录 用户登录 POST /api/user/login */
export async function loginApiUserLoginPost(
  body: API.UserLoginRequest,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseUserVO_>("/api/user/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    data: body,
    ...(options || {}),
  });
}

/** 用户退出登录 用户退出登录 POST /api/user/logout */
export async function logoutApiUserLogoutPost(
  // 叠加生成的Param类型 (非body参数swagger默认没有生成对象)
  params: API.logoutApiUserLogoutPostParams,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseBool_>("/api/user/logout", {
    method: "POST",
    params: { ...params },
    ...(options || {}),
  });
}

/** 用户注册 用户注册 POST /api/user/register */
export async function registerApiUserRegisterPost(
  body: API.UserRegisterRequest,
  options?: { [key: string]: any }
) {
  return request<API.BaseResponseUserVO_>("/api/user/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    data: body,
    ...(options || {}),
  });
}
