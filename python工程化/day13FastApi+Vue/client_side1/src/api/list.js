// 引入axios实例
import request from '@/api/request'

// 获取列表接口
export function getList(params) {
  return request({
    url: '/api/4/news/latest',
    method: 'get',
    params: params
  })
}
