import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DetectorView from '@/views/DetectorView.vue'
import ClassificatorView from '@/views/ClassificatorView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/detector',
      name: 'detector',
      component: DetectorView
    },
    {
      path: '/classificator',
      name: 'classificator',
      component: ClassificatorView
    }
  ]
})

export default router
