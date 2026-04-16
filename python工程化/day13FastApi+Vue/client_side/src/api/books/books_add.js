// 引入axios实例
import request from '@/api/request'

// 获取列表接口
export function addBook(data) {
  return request({
    url: '/api/books/add_book',
    method: 'post',
    data: data
  })
}