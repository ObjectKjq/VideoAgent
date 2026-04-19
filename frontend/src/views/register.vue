<script setup lang="ts">
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { message } from 'ant-design-vue'
import { registerApiUserRegisterPost } from '@/api/userRouter'

const router = useRouter()
const formState = reactive({
  userAccount: '',
  userPassword: '',
  checkPassword: '',
})

const onFinish = async (values: any) => {
  if (values.userPassword !== values.checkPassword) {
    message.error('两次输入的密码不一致')
    return
  }
  try {
    const res = await registerApiUserRegisterPost({
      userAccount: values.userAccount,
      userPassword: values.userPassword,
    })
    if (res.data.code === 0) {
      message.success('注册成功')
      router.push('/user/login')
    } else {
      message.error(res.data.message || '注册失败')
    }
  } catch (error) {
    message.error('注册失败，请稍后重试')
  }
}
</script>

<template>
  <div class="register-container">
    <a-card class="register-card">
      <h2>用户注册</h2>
      <a-form
        :model="formState"
        name="register"
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
        <a-form-item
          name="checkPassword"
          :rules="[{ required: true, message: '请确认密码' }]"
        >
          <a-input-password v-model:value="formState.checkPassword" placeholder="确认密码" size="large" />
        </a-form-item>
        <a-form-item>
          <a-button type="primary" html-type="submit" block size="large">
            注册
          </a-button>
        </a-form-item>
        <div class="login-link">
          已有账号？<router-link to="/user/login">立即登录</router-link>
        </div>
      </a-form>
    </a-card>
  </div>
</template>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f0f2f5;
}

.register-card {
  width: 400px;
}

h2 {
  text-align: center;
  margin-bottom: 24px;
}

.login-link {
  text-align: center;
  margin-top: 16px;
}
</style>
