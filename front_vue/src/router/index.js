import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '../views/IndexView.vue'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: IndexView,
      /*children: [
        { path: "", name: "Index", component: () => import("./views/Home") },
        { path: "foo", name: "Footer", component: () => import("./views/Foo") },
        { path: "bar", name: "navbar", component: () => import("./views/Bar") }
      ]*/
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    }
  ]
})

export default router
