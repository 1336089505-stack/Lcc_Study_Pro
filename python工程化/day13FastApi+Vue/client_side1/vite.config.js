import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    // 配置别名
    alias: {
      // 可以在vue组件中将@识别为src目录的地址
      // 可以通过@/xxxx 引入文件
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  // 对本地node.js服务做配置
  server: {
    // 配置服务器代理
    proxy: {
      // 识别 /api开头的请求
      // '/api': {
      //   // 接口的目标地址
      //   target: 'https://news-at.zhihu.com',
      //   // 是否允许跨域
      //   changeOrigin: true
      // }
      '/api': {
        // 接口的目标地址
        target: 'http://127.0.0.1',
        // 是否允许跨域
        changeOrigin: true
      }
    }
  }
})
