import request from "./request";


export function getProjectList(params) {
  return request({
    url: "/api/v1/project/list",
    method: "get",
    params,
  });
}
