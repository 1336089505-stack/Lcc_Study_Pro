import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'BookHome',
      component: () => import('../views/books/BookHome.vue'),
    },
    {
      path: '/book_add',
      name: 'BookAdd',
      component: () => import('../views/books/BookAdd.vue'),
    },
    {
      path: '/book_update',
      name: 'BookUpdate',
      component: () => import('../views/books/BookUpdate.vue'),
    },
  ],
})

export default router
