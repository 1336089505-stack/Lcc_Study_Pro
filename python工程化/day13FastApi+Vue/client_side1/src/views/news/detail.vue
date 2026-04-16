<template>
  <div class="news-detail-container">
    <div v-if="newsDetail" class="news-content">
      <h1 class="news-title">{{ newsDetail.title }}</h1>
      <div class="news-meta">
        <span class="news-source">来源：{{ newsDetail.source }}</span>
        <span class="news-publish-time">发布时间：{{ formatDate(newsDetail.publish_time) }}</span>
        <span class="news-comment-count">评论：{{ newsDetail.comment_count }}</span>
      </div>
      <div class="news-body">
        {{ newsDetail.content }}
      </div>
    </div>
    <div v-else class="loading">正在加载新闻详情...</div>

    <div class="comments-section">
      <h2>评论列表 ({{ comments.length }})</h2>
      <div v-if="comments.length > 0" class="comments-list">
        <div v-for="comment in comments" :key="comment.id" class="comment-item">
          <div class="comment-header">
            <h4 class="comment-author">{{ comment.name }}</h4>
            <span class="comment-time">{{ formatDate(comment.comment_time) }}</span>
          </div>
          <p class="comment-content">{{ comment.content }}</p>
          <div class="comment-footer">
            <span class="comment-likes">👍 {{ comment.likes }}</span>
            <button class="like-button" @click="likeComment(comment.id)">点赞</button>
          </div>
        </div>
      </div>
      <div v-else class="no-comments">暂无评论</div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getNewsCommentList, getNewsContent, newsCommentLikes } from '@/api/news'

export default {
  name: 'NewsDetail',
  setup() {
    const route = useRoute()
    const newsDetail = ref(null)
    const comments = ref([])

    const newsId = route.query.content_id

    // 获取新闻详情
    const fetchNewsDetail = async () => {
      try {
        const response = await getNewsContent({ content_id: newsId })
        if (response.code === 0) {
          newsDetail.value = response.data
        } else {
          console.error('获取新闻详情失败:', response.message)
        }
      } catch (error) {
        console.error('获取新闻详情出错:', error)
      }
    }

    // 获取评论列表
    const fetchComments = async () => {
      try {
        const response = await getNewsCommentList({ content_id: newsId })
        if (response.code === 0) {
          comments.value = response.data
        } else {
          console.error('获取评论列表失败:', response.message)
        }
      } catch (error) {
        console.error('获取评论列表出错:', error)
      }
    }

    // 点赞评论
    const likeComment = async (commentId) => {
      try {
        const response = await newsCommentLikes({ comment_id: commentId })
        if (response.code === 0 && response.data === true) {
          // 点赞成功后刷新评论列表
          await fetchComments()
          console.log('点赞成功')
        } else {
          console.error('点赞失败:', response.message)
          alert(`点赞失败: ${response.message}`)
        }
      } catch (error) {
        console.error('点赞出错:', error)
        alert('点赞失败，请稍后重试')
      }
    }

    // 格式化日期时间
    const formatDate = (dateString) => {
      const date = new Date(dateString)
      return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      })
    }

    onMounted(() => {
      fetchNewsDetail()
      fetchComments()
    })

    return {
      newsDetail,
      comments,
      formatDate,
      likeComment
    }
  }
}
</script>

<style scoped>
.news-detail-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  line-height: 1.6;
}

.news-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 15px;
  color: #333;
}

.news-meta {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  color: #666;
  font-size: 14px;
  border-bottom: 1px solid #eee;
  padding-bottom: 15px;
}

.news-body {
  margin-top: 20px;
  white-space: pre-wrap;
  color: #444;
  font-size: 16px;
  line-height: 1.8;
}

.comments-section {
  margin-top: 40px;
}

.comments-section h2 {
  border-left: 4px solid #409eff;
  padding-left: 10px;
  margin-bottom: 20px;
}

.comment-item {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 15px;
  background-color: #fafafa;
}

.comment-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.comment-author {
  font-weight: bold;
  color: #333;
  margin: 0;
}

.comment-time {
  color: #999;
  font-size: 14px;
}

.comment-content {
  margin: 10px 0;
  color: #555;
  line-height: 1.6;
}

.comment-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.comment-likes {
  color: #666;
  font-size: 14px;
}

.like-button {
  background-color: #42b883;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.like-button:hover {
  background-color: #36966f;
}

.loading, .no-comments {
  text-align: center;
  padding: 20px;
  color: #666;
}
</style>