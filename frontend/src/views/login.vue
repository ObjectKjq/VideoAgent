<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
const formState = reactive({
  userAccount: '',
  userPassword: '',
})

const onFinish = async (values: any) => {
  const result = await userStore.login(values.userAccount, values.userPassword)
  if (result.success) {
    message.success('登录成功')
    const redirect = new URLSearchParams(window.location.search).get('redirect') || '/'
    router.push(redirect)
  } else {
    message.error(result.message)
  }
}
</script>

<template>
  <div class="login-container">
    <a-card class="login-card">
      <h2>用户登录</h2>
      <a-form
        :model="formState"
        name="login"
        @finish="onFinish"
        layout="vertical"
      >
        <a-form-item
          name="userAccount"
          :rules="[{ required: true, message: '请输入账号' }]"
        >
          <a-input v-model:value="formState.userAccount" placeholder="账号" size="large" />
        </a-form-item>
        <a-form-item
          name="userPassword"
          :rules="[{ required: true, message: '请输入密码' }]"
        >
          <a-input-password v-model:value="formState.userPassword" placeholder="密码" size="large" />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" block size="large">
            登录
          </a-button>
        </a-form-item>
        <div class="register-link">
          还没有账号？<router-link to="/user/register">立即注册</router-link>
        </div>
      </a-form>
    </a-card>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f0f2f5;
}

.login-card {
  width: 400px;
}

h2 {
  text-align: center;
  margin-bottom: 24px;
}

.register-link {
  text-align: center;
  margin-top: 16px;
}
</style>
