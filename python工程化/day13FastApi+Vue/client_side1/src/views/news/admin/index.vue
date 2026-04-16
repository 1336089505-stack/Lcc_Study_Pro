<template>
  <div class="admin-container">
    <h2>新闻管理</h2>
    
    <!-- 添加新闻表单 -->
    <form @submit.prevent="submitForm" class="comment-form">
      <h3>添加新闻</h3>
      <div class="form-group">
        <label for="title">新闻标题:</label>
        <input
          id="title"
          type="text"
          v-model="form.title"
        />
        <small v-if="errors.title" class="error-message">{{ errors.title }}</small>
      </div>

      <div class="form-group">
        <label for="content">新闻内容:</label>
        <textarea
          id="content"
          v-model="form.content"
          rows="5"
        ></textarea>
        <small v-if="errors.content" class="error-message">{{ errors.content }}</small>
      </div>

      <div class="form-group">
        <label for="source">新闻来源:</label>
        <input
          id="source"
          type="text"
          v-model="form.source"
        />
        <small v-if="errors.source" class="error-message">{{ errors.source }}</small>
      </div>

      <div class="form-actions">
        <button
          type="submit"
          :disabled="submitting"
          class="btn-submit"
        >
          {{ submitting ? '提交中...' : '提交' }}
        </button>
        <button
          type="button"
          @click="resetForm"
          class="btn-reset"
        >
          重置
        </button>
      </div>
    </form>

    <!-- 新闻列表 -->
    <div class="news-list-section">
      <h3>新闻列表</h3>
      <div v-if="loading" class="loading">正在加载新闻数据...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      <div v-else class="news-list">
        <div v-for="item in newsList" :key="item.id" class="news-item">
          <div class="news-info">
            <div class="news-id">ID: {{ item.id }}</div>
            <h4 class="news-title">{{ item.title }}</h4>
            <p class="news-content">{{ item.content }}</p>
            <div class="news-meta">来源: {{ item.source }}</div>
          </div>
          <div class="news-actions">
            <button class="delete-btn" @click="deleteItem(item.id)">删除</button>
          </div>
        </div>
      </div>
      <div v-if="!loading && newsList.length === 0" class="no-data">
        暂无新闻数据
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, ref, onMounted } from 'vue'
import { newsCommentAdd, getNewsContentList, newsCommentDelete } from '@/api/news/index'

export default {
  name: 'NewsCommentAdmin',
  setup() {
    // 表单数据，设置默认值
    const form = reactive({
      title: '测试新闻',
      content: '这是测试新闻的内容',
      source: '测试来源'
    })

    // 错误信息
    const errors = reactive({
      title: '',
      content: '',
      source: ''
    })

    const submitting = ref(false)
    const newsList = ref([])
    const loading = ref(false)
    const error = ref(null)

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

    // 验证表单
    const validateForm = () => {
      // 清空之前的错误信息
      Object.keys(errors).forEach(key => errors[key] = '')

      let isValid = true

      // 验证标题
      if (!form.title.trim()) {
        errors.title = '新闻标题不能为空'
        isValid = false
      } else if (form.title.length < 2) {
        errors.title = '新闻标题长度不能少于2个字符'
        isValid = false
      } else if (form.title.length > 50) {
        errors.title = '新闻标题长度不能超过50个字符'
        isValid = false
      }

      // 验证内容
      if (!form.content.trim()) {
        errors.content = '新闻内容不能为空'
        isValid = false
      }

      // 验证来源
      if (!form.source.trim()) {
        errors.source = '新闻来源不能为空'
        isValid = false
      }

      return isValid
    }

    // 提交表单
    const submitForm = async () => {
      if (!validateForm()) {
        return
      }

      submitting.value = true
      try {
        const response = await newsCommentAdd(form)
        if (response.code === 0) {
          alert('新闻添加成功！')
          resetForm()
          // 添加成功后刷新列表
          await fetchNewsList()
        } else {
          alert(`添加失败: ${response.message}`)
        }
      } catch (error) {
        console.error('添加新闻时出错:', error)
        alert('提交失败，请稍后重试')
      } finally {
        submitting.value = false
      }
    }

    // 删除新闻项
    const deleteItem = async (id) => {
      if (confirm(`确定要删除ID为 ${id} 的新闻吗？此操作不可撤销。`)) {
        try {
          // 调用删除接口
          const response = await newsCommentDelete({ content_id: id })
          if (response.code === 0 && response.data === true) {
            // 成功删除后，刷新整个列表
            await fetchNewsList()
            alert('删除成功！')
          } else {
            alert(`删除失败: ${response.message}`)
          }
        } catch (err) {
          console.error('删除失败:', err)
          alert('删除失败，请稍后重试')
        }
      }
    }

    // 重置表单
    const resetForm = () => {
      form.title = '测试新闻'
      form.content = '这是测试新闻的内容'
      form.source = '测试来源'
      Object.keys(errors).forEach(key => errors[key] = '')
    }

    onMounted(() => {
      fetchNewsList()
    })

    return {
      form,
      errors,
      submitting,
      newsList,
      loading,
      error,
      submitForm,
      resetForm,
      deleteItem
    }
  }
}
</script>

<style scoped>
.admin-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.comment-form {
  margin: 20px 0;
  padding: 20px;
  border: 1px solid #eee;
  border-radius: 4px;
  background-color: #fafafa;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #333;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #409eff;
  box-shadow: 0 0 5px rgba(64, 158, 255, 0.3);
}

.form-actions {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}

.btn-submit,
.btn-reset {
  padding: 10px 20px;
  border: 1px solid transparent;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.btn-submit {
  background-color: #409eff;
  color: white;
}

.btn-submit:hover:not(:disabled) {
  background-color: #66b1ff;
}

.btn-submit:disabled {
  background-color: #a0cfff;
  cursor: not-allowed;
}

.btn-reset {
  background-color: #f4f4f5;
  color: #606266;
  border-color: #dcdfe6;
}

.btn-reset:hover {
  background-color: #ecf5ff;
  color: #409eff;
}

.error-message {
  color: #f56c6c;
  font-size: 12px;
  margin-top: 5px;
  display: block;
}

.news-list-section {
  margin-top: 30px;
}

.news-list-section h3 {
  margin-bottom: 15px;
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
  padding: 15px;
  background-color: #fff;
  transition: background-color 0.3s ease;
  cursor: pointer;
  position: relative;
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
  font-size: 16px;
  margin: 5px 0;
  color: #333;
  line-height: 1.4;
}

.news-content {
  font-size: 14px;
  color: #555;
  margin: 5px 0;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.news-meta {
  font-size: 12px;
  color: #888;
  margin-top: 5px;
}

.news-actions {
  display: flex;
  justify-content: flex-end;
  min-width: 80px;
  margin-left: 15px;
}

.delete-btn {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 8px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.3s ease;
}

.delete-btn:hover {
  background-color: #c0392b;
}

.loading,
.error,
.no-data {
  text-align: center;
  padding: 20px;
  font-size: 16px;
}

.error {
  color: #e74c3c;
}
</style>