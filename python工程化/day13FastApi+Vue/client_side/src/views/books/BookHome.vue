<script setup>
import { ref } from "vue";
import { getBooksList } from "@/api/books/books_select"
import { useRouter } from 'vue-router'
import { deleteBook } from "@/api/books/book_delete";

const router = useRouter()

const goAdd = () => {
  router.push('/book_add') // 路径和你路由保持一致
}

const book_list = ref({})

getBooksList().then((res) => {
  book_list.value = res.data
})

const delete_book = (id) => {
  deleteBook(id)
    .then(res => {
        alert('删除成功！')
        window.location.reload()
    })
    .catch(err => {
        alert('删除失败！')
        console.error(err)
    })
}

const update_book = (id) => {
  let list_value = book_list.value
   for (const value of list_value) {
  }
  router.push({
      path:'/book_update',
      query: {
        id: id
      }
    }
  )
  
}



</script>

<template>

<div class="page-container">
  <!-- 页面标题 -->
  <h2 class="page-title">书籍列表</h2>

  <div class="top-toolbar">
    <button class="btn btn-primary add-btn" @click="goAdd">
      + 新增书籍
    </button>
  </div>

  <div class="query-box">
    <!-- 书名查询 -->
    <div class="query-item">
      <label>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;书籍名称：</label>
      <input
        class="input-item"
        placeholder="请输入书名"
      />
    </div>
     <!-- 查询按钮 -->
    <button @click="getList" class="btn btn-primary">查询</button>

    <!-- 价格区间查询 -->
    <div class="query-item">
      <label>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;价格区间：</label>
      <input
        class="input-item small"
        placeholder="最低价"
        type="number"
      />
      <span class="line">-</span>
      <input
        class="input-item small"
        placeholder="最高价"
        type="number"
      />
    </div>

    <!-- 查询按钮 -->
    <button @click="getList" class="btn btn-primary">查询</button>
  </div>


  <div class="table-box">
    <table class="my-table">
      <thead>
        <tr>
          <th>书籍名称</th>
          <th>书籍分类</th>
          <th>书籍装帧</th>
          <th>书籍标签</th>
          <th>书籍价格</th>
          <th>是否在售</th>
          <th>操作</th>
        </tr>
      </thead>
        <tbody v-for="book in book_list" :key="book.id">
          <tr>
            <td>{{ book.name }}</td>
            <td>{{ book.category }}</td>
            <td>{{ book.binding }}</td>
            <td>{{ book.tags }}</td>
            <td>{{ book.price }}</td>
            <td>{{ book.is_sale ? '在售' : '下架' }}</td>
            <td>
            <button class="btn-edit" @click="update_book(book.id)">编辑</button>
            <button class="btn-del" @click="delete_book(book.id)">删除</button>
            </td>
          </tr>
        </tbody>
    </table>
  </div>

  <!-- 分页区域 -->
  <div class="pagination">
    <button :disabled="currentPage === 1" @click="currentPage--">上一页</button>
    <button
      v-for="page in totalPages"
      :key="page"
      :class="{ active: currentPage === page }"
      @click="currentPage = page; getList()"
    >
      {{ page }}
    </button>
    <button :disabled="currentPage === totalPages" @click="currentPage++">下一页</button>
  </div>
</div>
</template>


<style scoped>
</style>