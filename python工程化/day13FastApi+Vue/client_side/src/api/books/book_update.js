// 引入axios实例
import request from '@/api/request'

// 获取列表接口
export function updateBook(params) {
  return request({
    url: '/api/books/update_book',
    method: 'post',
    data: params
  })
}