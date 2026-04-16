import request from "./request";

export function getCategoryList() {
  return request({
    url: "/api/v1/category/list",
    method: "get",
  });
}

export function findCategoryList(params) {
  return request({
    url: "/api/v1/category/list/find",
    method: "post",
    data: params,
  });
}
