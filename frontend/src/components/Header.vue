<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import { message } from "ant-design-vue";
import { UserOutlined, LogoutOutlined } from "@ant-design/icons-vue";
import logoImg from "@/assets/logo.png";

const router = useRouter();
const userStore = useUserStore();
const selectedKeys = ref<string[]>([]);

onMounted(() => {
  if (!userStore.user) {
    userStore.fetchCurrentUser();
  }
});

const handleLogout = async () => {
  await userStore.logout();
  message.success("已退出登录");
  router.push("/user/login");
};
</script>

<template>
  <a-layout-header class="header">
    <div class="header-content">
      <div class="logo" @click="router.push('/')">
        <img :src="logoImg" alt="Logo" class="logo-img" />
        <span>视频生成器</span>
      </div>
      <a-menu
        v-model:selectedKeys="selectedKeys"
        mode="horizontal"
        class="nav-menu"
      >
        <a-menu-item key="home" @click="router.push('/')">首页</a-menu-item>
      </a-menu>
      <div class="header-actions">
        <template v-if="userStore.isLoggedIn && userStore.user">
          <a-dropdown>
            <div class="user-info">
              <a-avatar
                :size="32"
                :src="userStore.user.userAvatar"
                class="user-avatar"
              >
                <template #icon>
                  <UserOutlined />
                </template>
              </a-avatar>
              <span class="user-name">{{
                userStore.user.userName || userStore.user.userAccount
              }}</span>
            </div>
            <template #overlay>
              <a-menu>
                <a-menu-item key="logout" @click="handleLogout">
                  <LogoutOutlined />
                  <span style="margin-left: 8px">退出登录</span>
                </a-menu-item>
              </a-menu>
            </template>
          </a-dropdown>
        </template>
        <template v-else>
          <a-button type="link" @click="router.push('/user/login')"
            >登录</a-button
          >
          <a-button type="link" @click="router.push('/user/register')"
            >注册</a-button
          >
        </template>
      </div>
    </div>
  </a-layout-header>
</template>

<style scoped>
.header {
  background: #fff;
  padding: 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.header-content {
  display: flex;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  height: 100%;
  padding: 0 24px;
}

.logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 18px;
  font-weight: bold;
  color: #1890ff;
  cursor: pointer;
  margin-right: 24px;
}

.logo-img {
  height: 32px;
  width: auto;
}

.nav-menu {
  flex: 1;
  background: transparent;
  border-bottom: none;
}

.header-actions {
  display: flex;
  gap: 8px;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.user-info:hover {
  background-color: rgba(0, 0, 0, 0.04);
}

.user-avatar {
  background-color: #1890ff;
}

.user-name {
  color: rgba(0, 0, 0, 0.85);
  font-size: 14px;
}
</style>
