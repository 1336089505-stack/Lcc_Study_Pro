// 引入axios实例
import request from '@/api/request'

// 获取列表接口
export function getBooksList(params) {
  return request({
    url: '/api/books/home',
    method: 'get',
    params: params
  })
}

export function getBookDetail(id) {
  return request({
    url: '/api/books/bookDetail',
    method: 'get', 
     params: {id: id} 
  })
}

