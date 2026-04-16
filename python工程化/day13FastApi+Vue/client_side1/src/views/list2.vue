<template>
  <div class="list">
    <h1>列表2</h1>
    <!-- 列表项 v-for接收一个数组，对数组中的每一项进行循环渲染 -->
    <!-- 使用ref定义的变量 json，json接收接口数据 -->
    <div class="item" v-for="item in json.stories" :key="item">
      <div class="left">
        <a :href="item.url">{{ item.title }}</a>
        <div>{{ item.hint }}</div>
      </div>
      <div class="right">
        <img :src="item.images[0]" alt="">
      </div>
    </div>
  </div>
</template>

<script setup>
// 引入接口方法 getList
import { getList } from "@/api/list";
import { ref } from "vue";

// 通过ref方法定义变量，数据更新时，将触发页面重渲染
const json = ref({});

// 调用接口方法，获取接口数据
getList({ num: "列表业务相关数据" }).then((res) => {
  console.log(res);
  // 接口数据保存在变量json中
  json.value = res;
})

/*
request({
    url: '/api/4/news/latest',
    method: 'get'
  }).then((res) => {
  // 这里拿到数据
  })
*/
</script>

<style>
.list {}

.item {
  width: 654px;
  display: flex;
  justify-content: space-between;
  background: red;
}

.left {
  width: 404px;
  height: 105px;
  background: rgb(115, 255, 0);
}

.right {
  width: 190px;
  height: 105px;
  margin-left: 16px;
  margin-right: 16px;
  background: yellow;
}

img {
  width: 190px;
  height: 105px;
}
</style>
