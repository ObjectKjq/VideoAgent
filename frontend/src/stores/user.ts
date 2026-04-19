import { ref, computed } from "vue";
import { defineStore } from "pinia";
import {
  getCurrentApiUserCurrentGet,
  loginApiUserLoginPost,
  logoutApiUserLogoutPost,
} from "@/api/userRouter";

type UserVO = {
  id: number;
  userAccount: string;
  userName?: string | null;
  userAvatar?: string | null;
  userProfile?: string | null;
  userRole: string;
  createTime?: string | null;
  updateTime?: string | null;
};

export const useUserStore = defineStore("user", () => {
  const user = ref<UserVO | null>(null);
  const isLoggedIn = computed(() => !!user.value);

  async function fetchCurrentUser() {
    try {
      const res = await getCurrentApiUserCurrentGet({});
      if (res.data.code === 0 && res.data.data) {
        user.value = res.data.data;
        return true;
      }
      return false;
    } catch {
      return false;
    }
  }

  async function login(userAccount: string, userPassword: string) {
    try {
      const res = await loginApiUserLoginPost({ userAccount, userPassword });
      if (res.data.code === 0 && res.data.data) {
        user.value = res.data.data;
        return { success: true, message: "登录成功" };
      }
      return { success: false, message: res.data.message || "登录失败" };
    } catch (error: any) {
      return { success: false, message: error.message || "登录失败" };
    }
  }

  async function logout() {
    try {
      await logoutApiUserLogoutPost({});
    } catch {
    } finally {
      user.value = null;
    }
  }

  function clearUser() {
    user.value = null;
  }

  return {
    user,
    isLoggedIn,
    fetchCurrentUser,
    login,
    logout,
    clearUser,
  };
});
