<template>
  <div class="page-container">
    <h2 class="page-title">新增书籍</h2>

    <div class="form-container">
        <!-- 1. 书籍名称（必填） -->
        <div class="form-item">
        <label class="form-label required">书籍名称</label>
        <input
          class="form-input"
          v-model="form.name"
          placeholder="请输入书籍名称"
        />
        <!-- 错误提示 -->
        <div v-if="errors.name" class="form-error">{{ errors.name }}</div>
        </div>

        <!-- 2. 书籍分类（下拉框，固定6个选项） -->
        <div class="form-item">
        <label class="form-label required">书籍分类</label>
        <select class="form-select" v-model="form.category">
          <option value="">请选择分类</option>
          <option value="文学小说">文学小说</option>
          <option value="历史传记">历史传记</option>
          <option value="科普读物">科普读物</option>
          <option value="人文社科">人文社科</option>
          <option value="少儿绘本">少儿绘本</option>
          <option value="计算机技术">计算机技术</option>
        </select>
        <div v-if="errors.category" class="form-error">{{ errors.category }}</div>
        </div>

        <!-- 3. 书籍装帧（单选框，3个选项，必选） -->
        <div class="form-item">
        <label class="form-label required">书籍装帧</label>
        <div class="radio-group" >
          <label class="radio-item">
            <input
              type="radio"
              value="平装"
              name="binding"
              v-model="form.binding"
            />
            <span>平装</span>
          </label>
          <label class="radio-item">
            <input
              type="radio"
              value="精装"
              name="binding"
              v-model="form.binding"
            />
            <span>精装</span>
          </label>
          <label class="radio-item">
            <input
              type="radio"
              value="线装"
              name="binding"
              v-model="form.binding"
            />
            <span>线装</span>
          </label>
        </div>
        <div v-if="errors.binding" class="form-error">{{ errors.binding }}</div>
      </div>

      <!-- 4. 书籍标签（复选框，6个选项，至少选1个） -->
      <div class="form-item">
        <label class="form-label required">书籍标签</label>
        <div class="checkbox-group">
          <label class="checkbox-item" v-for="tag in tagOptions" :key="tag.value">
            <input
              type="checkbox"
              :value="tag.value"
                v-model="form.tags"
                name="tags_{{tag.value}}"
            />
            <span>{{ tag.label }}</span>
          </label>
        </div>
        <div v-if="errors.tags" class="form-error">{{ errors.tags }}</div>
      </div>

      <!-- 5. 价格 -->
      <div class="form-item">
        <label class="form-label required">价格</label>
        <input
          v-model.number="form.price"
          class="form-input"
          type="number"
          step="0.01"
          min="0"
          placeholder="请输入价格"
        />
        <div v-if="errors.price" class="form-error">{{ errors.price }}</div>
      </div>

      <!-- 6. 是否在售（单选框，2个选项，必选） -->
      <div class="form-item">
        <label class="form-label required">是否在售</label>
        <div class="radio-group">
          <label class="radio-item">
            <input
              type="radio"
              :value="true"
              name="is_sale"
              v-model="form.is_sale"
            />
            <span>是</span>
          </label>
          <label class="radio-item">
            <input
              type="radio"
              :value="false"
              name="is_sale"
              v-model="form.is_sale"
            />
            <span>否</span>
          </label>
        </div>
        <div v-if="errors.is_sale" class="form-error">{{ errors.is_sale }}</div>
      </div>


      <!-- 按钮区域 -->
      <div class="form-footer">
        <button class="btn btn-default" @click="goBack">返回</button>
        <button class="btn btn-primary" @click="submitForm">提交保存</button>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { addBook } from "@/api/books/books_add"
const router = useRouter()

const tagOptions = ref([
  { value: '经典名著', label: '经典名著' },
  { value: '畅销书', label: '畅销书' },
  { value: '新书上架', label: '新书上架' },
  { value: '限时折扣', label: '限时折扣' },
  { value: '青少年推荐', label: '青少年推荐' }
])

const form = ref({
  name: '',
  category:'',
  binding:'',
  tags:[],
  price:0,
  is_sale: true
})

// ====================== 新增：错误提示 ======================
const errors = ref({
  name: '',
  category: '',
  binding: '',
  tags: '',
  price: '',
  is_sale: ''
})

// 校验函数
const validateForm = () => {
  let valid = true
  errors.value = {} // 清空错误

  if (!form.value.name.trim()) {
    errors.value.name = '请输入书籍名称'
    valid = false
  }
  if (!form.value.category) {
    errors.value.category = '请选择书籍分类'
    valid = false
  }
  if (!form.value.binding) {
    errors.value.binding = '请选择书籍装帧'
    valid = false
  }
  if (!form.value.tags || form.value.tags.length === 0) {
    errors.value.tags = '至少选择一个标签'
    valid = false
  }
  if (form.value.price <= 0) {
    errors.value.price = '价格必须大于0'
    valid = false
  }
  if (form.value.is_sale === null || form.value.is_sale === undefined) {
    errors.value.is_sale = '请选择是否在售'
    valid = false
  }

  return valid
}
// ==========================================================

const goBack = () => {
  router.push('/')
}

const submitForm = () => {
  // 新增：提交前校验
  if (!validateForm()) return

  addBook(form.value)
  .then(res => {
      alert('新增书籍成功！')
      goBack()
  })
  .catch(err => {
      alert('新增失败，请检查数据')
      console.error(err)
  })
}

</script>

<style scoped>
/* 全局页面容器 */
.page-container {
  padding: 20px;
}

/* 表单容器 */
.form-container {
  background: #fff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  max-width: 800px;
  margin: 0 auto;
}

/* 表单项 */
.form-item {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-size: 14px;
  font-weight: bold;
  color: #333;
}

.form-label.required:after {
  content: "*";
  color: #e74c3c;
  margin-left: 4px;
}

/* 输入框 */
.form-input,
.form-select,
.form-textarea {
  width: 100%;
  height: 38px;
  padding: 0 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  outline: none;
}

.form-textarea {
  height: auto;
  padding: 10px 12px;
  resize: vertical;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  border-color: #3498db;
  box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.1);
}

/* 错误提示 👇 样式已存在，我直接用了 */
.form-error {
  color: #e74c3c;
  font-size: 12px;
  margin-top: 4px;
}

/* 按钮区域 */
.form-footer {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 30px;
}

/* 按钮样式 */
.btn {
  height: 38px;
  padding: 0 20px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: #3498db;
  color: #fff;
}

.btn-default {
  background: #ecf0f1;
  color: #333;
}
</style>