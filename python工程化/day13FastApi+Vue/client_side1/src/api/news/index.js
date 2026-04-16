// 引入axios实例
import request from '@/api/request'

// 获取列表接口
export function getNewsContentList(params) {
  return request({
    url: '/api/v1/news_content/list',
    method: 'get',
    params: params
  })
}
export function getNewsContent(params) {
  return request({
    url: '/api/v1/news_content/get',
    method: 'get',
    params: params
  })
}

export function getNewsCommentList(params) {
  return request({
    url: '/api/v1/news_comment/list',
    method: 'get',
    params: params
  })
}

export function newsCommentAdd(params) {
  return request({
    url: '/api/v1/admin/add',
    method: 'post',
    data: params
  })
}

export function newsCommentDelete(params) {
  return request({
    url: '/api/v1/admin/del',
    method: 'get',
    params: params
  })
}

export function newsCommentLikes(params) {
  return request({
    url: '/api/v1/news_comment/likes',
    method: 'get',
    params: params
  })
}
