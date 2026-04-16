// 引入axios实例
import request from '@/api/request'

export function deleteBook(id) {
  return request({
    url: '/api/books/delete_book',
    method: 'post', 
    data: {id: id}
  })
}