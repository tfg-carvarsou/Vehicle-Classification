import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ModelsView from '@/views/ModelsView.vue'
import DetectorView from '@/views/DetectorView.vue'
import ClassifierView from '@/views/ClassifierView.vue'
import TermsView from '@/views/TermsView.vue'
import PrivacyView from '@/views/PrivacyView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/models',
      name: 'models',
      component: ModelsView
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
    },
    {
      path: '/terms-of-service',
      name: 'terms',
      component: TermsView
    },
    {
      path: '/privacy-policy',
      name: 'privacy',
      component: PrivacyView
    }
  ]
})

export default router
