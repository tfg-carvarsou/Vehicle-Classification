import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import DetectorView from '@/views/DetectorView.vue'
import ClassifierView from '@/views/ClassifierView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/detector/snapzone',
      name: 'detector',
      component: DetectorView
    },
    {
      path: '/classifier/snapzone',
      name: 'classifier',
      component: ClassifierView
    }
  ]
})

export default router
