<template>
  <div class="list">
    <h1>列表1</h1>
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
  // 引入json数据，通过本地数据模拟接口数据
// import json from "../assets/jsonData.json";

// 引入axios库 用来接口调用
import axios from "axios";
import { ref } from "vue";

// 通过ref方法定义变量，数据更新时，将触发页面重渲染
const json = ref({});

// 发送get请求
axios.get("/api/4/news/latest").then(function (response) {
  // 将接口数据赋值给json变量
  json.value = response.data;
});

// 演示别名用法
// import HelloWorld from "@/components/HelloWorld.vue";
// console.log(HelloWorld);
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
