import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import axios from 'axios'

// 配置Axios基础URL
axios.defaults.baseURL = 'http://localhost:8000/api'

// 添加请求拦截器
axios.interceptors.request.use(config => {
  // 从localStorage获取token
  const token = localStorage.getItem('token')
  if (token) {
    // 添加token到请求头
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// 创建应用实例
const app = createApp(App)

// 使用路由
app.use(router)

// 挂载应用
app.mount('#app')
