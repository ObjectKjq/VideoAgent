<script setup lang="ts">
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
</script>

<template>
  <a-layout class="main-layout">
    <Header />
    <a-layout-content class="content">
      <router-view />
    </a-layout-content>
    <Footer />
  </a-layout>
</template>

<style scoped>
.main-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.content {
  flex: 1;
  background: #f0f2f5;
}
</style>
