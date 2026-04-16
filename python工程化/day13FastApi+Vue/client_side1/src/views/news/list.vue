<template>
  <div class="news-list-container">
    <h1>新闻列表</h1>

    <div v-if="loading" class="loading">正在加载新闻数据...</div>

    <div v-else-if="error" class="error">{{ error }}</div>

    <div v-else class="news-list">
      <div v-for="item in newsList" :key="item.id" class="news-item">
        <div class="news-info">
          <div class="news-id">ID: {{ item.id }}</div>
          <h3 class="news-title">{{ item.title }}</h3>
        </div>
        <div class="news-actions">
          <button class="view-btn" @click="goToDetail(item.id)">查看详情</button>
        </div>
      </div>
    </div>

    <!-- 如果没有数据 -->
    <div v-if="!loading && newsList.length === 0" class="no-data">
      暂无新闻数据
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getNewsContentList } from "@/api/news/index"

const newsList = ref([])
const loading = ref(false)
const error = ref(null)
const router = useRouter()

// 获取新闻列表
const fetchNewsList = async () => {
  loading.value = true
  error.value = null

  try {
    const response = await getNewsContentList()
    if (response.data) {
      newsList.value = response.data
    } else {
      throw new Error(response.message || '获取新闻列表失败')
    }
  } catch (err) {
    console.error('获取新闻列表失败:', err)
    error.value = err.message || '获取新闻列表失败'
  } finally {
    loading.value = false
  }
}

// 跳转到详情页
const goToDetail = (id) => {
  router.push({
    path: '/news/detail',
    query: {
      content_id: id
    }
  })
}

onMounted(() => {
  fetchNewsList()
})
</script>

<style scoped>
.news-list-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.loading,
.error,
.no-data {
  text-align: center;
  padding: 40px 20px;
  font-size: 18px;
}

.error {
  color: #e74c3c;
}

.news-list {
  display: flex;
  flex-direction: column;
  gap: 1px;
  background-color: #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
}

.news-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #fff;
  transition: background-color 0.3s ease;
  cursor: pointer;
  position: relative;
}

.news-item.bordered::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 20px;
  right: 20px;
  height: 1px;
  background-color: #e0e0e0;
}

.news-item:hover {
  background-color: #f8f8f8;
}

.news-info {
  flex: 1;
}

.news-id {
  font-size: 14px;
  color: #666;
  margin-bottom: 5px;
}

.news-title {
  font-size: 18px;
  margin: 0;
  color: #333;
  line-height: 1.4;
}

.news-actions {
  display: flex;
  justify-content: flex-end;
  min-width: 100px;
  margin-left: 15px;
  gap: 8px;
}

.view-btn {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
  min-width: 80px;
}

.view-btn:hover {
  background-color: #36966f;
}

.delete-btn {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
  min-width: 60px;
  margin-left: 5px;
}

.delete-btn:hover {
  background-color: #c0392b;
}

/* 在小屏幕上调整布局 */
@media (max-width: 768px) {
  .news-item {
    flex-direction: column;
    align-items: flex-start;
  }

  .news-actions {
    width: 100%;
    justify-content: flex-end;
    margin-top: 15px;
  }
}
</style>
