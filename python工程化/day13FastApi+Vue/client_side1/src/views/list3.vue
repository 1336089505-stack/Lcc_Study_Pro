<template>
  <div class="list">
    <div class="search-container">
      <div class="search-input-wrapper">
        <input type="text" v-model="queryParams.name" placeholder="请输入类型名称..." @keyup.enter="handleSearch"
          class="search-input" />
        <button @click="clearSearch" v-if="queryParams.name" class="clear-btn">✕</button>
      </div>
      <button @click="handleSearch" class="search-btn">搜索</button>
    </div>

    <div class="item" v-for="item in list.data" :key="item.id || item.name">
      <div class="content" @click="goProject(item.id)">
        <div class="id-box">{{ item.id }}</div>
        <h3 class="name">{{ item.name }}</h3>
        <p class="emoji">{{ item.emoji }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { findCategoryList } from "@/api/list3";
import { onMounted, ref, reactive } from "vue";
import router from "@/router";

const list = ref({ data: [] });
const queryParams = ref({
  name: '',
});

onMounted(() => {
  // 默认加载所有分类
  handleSearch();
});

const handleSearch = () => {
  findCategoryList(queryParams.value).then((res) => {
    console.log(res);
    list.value = res;
  }).catch(error => {
    console.error('Failed to search category list:', error);
  });
};

const clearSearch = () => {
  queryParams.value = {
    name: '',
  };
  handleSearch(); // 清空后重新搜索，显示全部结果
};

const goProject = (id) => {
  router.push({
    path: "/list4",
    query: {
      id: id
    }
  })
}
</script>

<style scoped>
.list {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.search-container {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  align-items: center;
}

.search-input-wrapper {
  position: relative;
  flex: 1;
}

.search-input {
  width: 80%;
  padding: 0.8rem 3rem 0.8rem 1rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.search-input:focus {
  outline: none;
  border-color: #409eff;
  box-shadow: 0 0 0 2px rgba(64, 158, 255, 0.2);
}

.clear-btn {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 16px;
  cursor: pointer;
  color: #999;
  padding: 4px;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.clear-btn:hover {
  background: #f0f0f0;
  color: #666;
}

.search-btn {
  padding: 0.8rem 1.5rem;
  background: #409eff;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.3s;
  min-width: 70px;
}

.search-btn:hover {
  background: #66b1ff;
}

.item {
  display: flex;
  align-items: center;
  padding: 1.2rem;
  margin-bottom: 1rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background: white;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.content {
  display: flex;
  align-items: center;
  width: 100%;
  cursor: pointer;
}

.id-box {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 40px;
  width: 40px;
  height: 40px;
  margin-right: 1rem;
  background-color: #f0f0f0;
  border-radius: 6px;
  font-weight: bold;
  color: #666;
  font-size: 1rem;
}

.name {
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
  margin: 0;
  flex: 1;
}

.emoji {
  font-size: 1.5rem;
  margin: 0 0 0 1rem;
  min-width: 50px;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
