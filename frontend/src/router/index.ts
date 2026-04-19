import { createRouter, createWebHistory } from "vue-router";
import MainLayout from "../layouts/MainLayout.vue";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: MainLayout,
      children: [
        {
          path: "",
          name: "home",
          component: HomeView,
        },
      ],
    },
    {
      path: "/user/login",
      name: "login",
      component: () => import("../views/login.vue"),
    },
    {
      path: "/user/register",
      name: "register",
      component: () => import("../views/register.vue"),
    },
  ],
});

export default router;
