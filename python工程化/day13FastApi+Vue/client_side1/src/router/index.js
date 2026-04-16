import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/list',
      name: 'list',
      component: () => import('../views/list.vue'),
    },
    {
      path: '/list2',
      name: 'list2',
      component: () => import('../views/list2.vue'),
    },
    {
      path: '/ai/list',
      name: 'list3',
      component: () => import('../views/ai/list.vue'),
    },
    {
      path: '/ai/detail',
      name: 'list4',
      component: () => import('../views/ai/detail.vue'),
    },
    {
      path: '/news/list',
      name: 'news_list',
      component: () => import('../views/news/list.vue'),
    },
    {
      path: '/news/detail',
      name: 'news_detail',
      component: () => import('../views/news/detail.vue'),
    },
        {
      path: '/news/admin',
      name: 'news_admin',
      component: () => import('../views/news/admin/index.vue'),
    },
  ],
})

export default router
