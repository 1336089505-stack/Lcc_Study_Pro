<template>
  <div class="list">
    <div class="header-actions">
      <button class="back-btn" @click="$router.go(-1)">
        ← 返回上一页
      </button>
    </div>

    <div class="item" v-for="item in list.data" :key="item.name">
      <div class="content">
        <div class="info">
          <div class="header">
            <h3 class="name">{{ item.name }}</h3>
            <!-- 将按钮移到这里不再需要 -->
          </div>

          <div class="meta">
            <div class="meta-item">
              <span class="label">⭐ 星级:</span>
              <span class="value">{{ item.star }}</span>
            </div>
            <div class="meta-item">
              <span class="label">👁️ 浏览:</span>
              <span class="value">{{ item.views }}</span>
            </div>
            <div class="meta-item">
              <span class="label">📅 日期:</span>
              <span class="value">{{ item.added_on }}</span>
            </div>
            <div class="meta-item">
              <span class="label">🔗 链接:</span>
              <span class="value">{{ item.link }}</span>
            </div>
            <div class="meta-item">
              <span class="label">📝 介绍:</span>
              <span class="value">{{ item.introduction }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 完整详情展开区域 -->
      <transition name="slide">
        <div v-show="expandedItem === item" class="detail-content">
          <div class="detail-section">
            <div class="detail-controls">
              <button
                class="detail-btn"
                @click="toggleDetail(item)"
              >
                {{ expandedItem === item ? '收起详情' : '查看完整详情' }}
              </button>
            </div>
            <p><strong>完整详情:</strong></p>
            <div class="full-detail">{{ item.detail }}</div>
          </div>
        </div>
      </transition>

      <!-- 默认显示两行详情 -->
      <div class="summary-content" v-if="!expandedItem || expandedItem !== item">
        <div class="summary-controls">
          <button
            class="detail-btn"
            @click="toggleDetail(item)"
          >
            {{ expandedItem === item ? '收起详情' : '查看完整详情' }}
          </button>
        </div>
        <p><strong>详情:</strong></p>
        <div class="summary-detail">{{ truncateText(item.detail, 100) }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { getProjectList } from "@/api/list4";
import { onMounted, ref } from "vue";
import { useRoute } from "vue-router";

const list = ref({ data: [] });
const route = useRoute();
const expandedItem = ref(null);

onMounted(() => {
  console.log(route.query.id);
  getProjectList({category_id: route.query.id}).then((res) => {
    console.log(res);
    list.value = res;
  }).catch(error => {
    console.error('Failed to load project list:', error);
  });
});

const toggleDetail = (item) => {
  // 如果点击的是当前展开的项目，则收起；否则切换到新的项目
  expandedItem.value = expandedItem.value === item ? null : item;
};

const truncateText = (text, maxLength) => {
  if (!text) return '';
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
};
</script>

<style scoped>
.list {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.header-actions {
  margin-bottom: 1.5rem;
  text-align: left;
}

.back-btn {
  background-color: #6c757d;
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.95rem;
  transition: background-color 0.2s;
  display: inline-flex;
  align-items: center;
}

.back-btn:hover {
  background-color: #5a6268;
}

.item {
  position: relative;
  display: flex;
  flex-direction: column;
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
  width: 100%;
  margin-bottom: 0.8rem;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.name {
  font-size: 1.2rem;
  font-weight: 600;
  color: #333;
  margin: 0;
  flex: 1;
  margin-right: 1rem;
}

.detail-btn {
  background-color: #409eff;
  color: white;
  border: none;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.85rem;
  transition: background-color 0.2s;
  align-self: flex-start;
}

.detail-btn:hover {
  background-color: #2a7be0;
}

.meta {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 0.8rem;
  width: 100%;
}

.meta-item {
  display: flex;
  flex-wrap: wrap;
  padding: 0.4rem 0;
  border-bottom: 1px solid #f5f5f5;
}

.label {
  font-weight: 600;
  color: #555;
  min-width: 60px;
  margin-right: 0.5rem;
  flex-shrink: 0;
}

.value {
  color: #666;
  flex: 1;
  word-break: break-word;
}

.summary-content {
  padding: 0 0.5rem;
  border-top: 1px solid #eee;
  margin-top: 0.8rem;
}

.summary-detail {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.5;
  color: #555;
  margin-top: 0.5rem;
}

.detail-content {
  padding: 0 0.5rem;
  border-top: 1px solid #eee;
  margin-top: 0.8rem;
}

.detail-section {
  padding: 1rem 0;
}

.detail-section p {
  margin: 0.8rem 0;
  line-height: 1.5;
  color: #555;
}

.full-detail {
  line-height: 1.5;
  color: #555;
  margin-top: 0.5rem;
  white-space: pre-line;
}

.detail-section p strong {
  color: #333;
  min-width: 80px;
  display: inline-block;
}

/* 新增样式：控制按钮位置 */
.summary-controls,
.detail-controls {
  margin-bottom: 0.5rem;
  text-align: right;
}

.detail-section p strong {
  color: #333;
  min-width: 80px;
  display: inline-block;
}

/* 展开/收起动画 */
.slide-enter-active {
  max-height: 400px;
  transition: max-height 0.3s ease-out;
  overflow: hidden;
}

.slide-leave-active {
  max-height: 400px;
  transition: max-height 0.2s ease-in;
  overflow: hidden;
}

.slide-enter-from {
  max-height: 0;
  opacity: 0;
}

.slide-leave-to {
  max-height: 0;
  opacity: 0;
}

@media (min-width: 768px) {
  .item {
    padding: 1.5rem;
  }

  .name {
    font-size: 1.3rem;
  }

  .meta {
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  }
}
</style>
