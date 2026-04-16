// 1.引入 axios库
import axios from 'axios'

// 2. 创建axios实例
const request = axios.create({
  // baseURL: '', //  接口的基准地址
  timeout: 5000 // 接口的超时时间
})


// 3.创建 请求拦截器
request.interceptors.request.use(
  (config) => {
    // 将用户的登录信息（token）统一发送给服务器
     console .log("请求拦截器 数据发送成功",config)
    return config
  },
  (error) => {
    console .log("请求拦截器 数据发送失败")
    return Promise.reject(error)
  }
)

// 4.创建 响应拦截器
 request.interceptors.response.use(
  (response) => {
    //  拦截所有响应
    // 如果服务器返回登录token失效，就跳转登录页
    console .log("响应拦截器 数据获取成功")
    return response.data
  },
  (error) => {
     console .log("响应拦截器 数据获取失败")
    return Promise.reject(error)
  }
)

// 将 axios实例导出
 export default request
