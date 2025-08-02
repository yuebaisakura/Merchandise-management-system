<template>
  <div class="product-list-container">
    <h2 class="page-title">商品列表</h2>
    <div class="action-bar">
      <button @click="navigateToAddProduct" class="add-button">添加商品</button>
    </div>
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="error" class="error-message">{{ error }}</div>
    <div v-else class="product-table-container">
      <table class="product-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>名称</th>
            <th>价格</th>
            <th>库存</th>
            <th>创建时间</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>¥{{ product.price }}</td>
            <td>{{ product.stock }}</td>
            <td>{{ formatDate(product.created_at) }}</td>
            <td class="action-buttons">
              <button @click="navigateToEditProduct(product.id)" class="edit-button">编辑</button>
              <button @click="deleteProduct(product.id)" class="delete-button">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { productAPI } from '../../api/product';

export default {
  name: 'ProductList',
  data() {
    return {
      products: [],
      loading: true,
      error: ''
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        this.loading = true;
        this.error = '';
        const response = await productAPI.getAllProducts();
        this.products = response.data;
      } catch (err) {
        this.error = err.response?.data?.detail || '获取商品列表失败';
      } finally {
        this.loading = false;
      }
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleString();
    },
    navigateToAddProduct() {
      this.$router.push('/products/add');
    },
    navigateToEditProduct(id) {
      this.$router.push(`/products/edit/${id}`);
    },
    async deleteProduct(id) {
      if (confirm('确定要删除这个商品吗？')) {
        try {
          await productAPI.deleteProduct(id);
          // 删除成功后刷新列表
          this.fetchProducts();
        } catch (err) {
          this.error = err.response?.data?.detail || '删除商品失败';
        }
      }
    }
  }
};
</script>

<style scoped>
.product-list-container {
  padding: 1rem;
  max-width: 100%;
  margin: 0 auto;
  box-sizing: border-box;
}

.page-title {
  color: #333;
  margin-bottom: 20px;
  font-size: 24px;
}

.action-bar {
  margin-bottom: 20px;
  text-align: right;
}

.add-button {
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 16px;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.add-button:hover {
  background-color: #3aa876;
}

.loading {
  text-align: center;
  padding: 20px;
  color: #666;
}

.error-message {
  color: #e74c3c;
  padding: 10px;
  background-color: #fadbd8;
  border-radius: 4px;
  margin-bottom: 20px;
}

.product-table-container {
  overflow-x: auto;
}

.product-table {
  width: 100%;
  border-collapse: collapse;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.product-table th,
.product-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.product-table th {
  background-color: #f5f7fa;
  font-weight: 600;
  color: #333;
}

.product-table tr:hover {
  background-color: #f9f9f9;
}

.action-buttons {
  display: flex;
  gap: 8px;
}

.edit-button {
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 6px 12px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.edit-button:hover {
  background-color: #2980b9;
}

.delete-button {
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 6px 12px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.delete-button:hover {
  background-color: #c0392b;
}

/* 响应式表格调整 */
@media (max-width: 768px) {
  .product-table-container {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .product-table {
    min-width: 600px;
  }

  .action-bar {
    text-align: left;
    margin-bottom: 1rem;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.25rem;
  }

  .action-buttons {
    flex-direction: column;
    gap: 0.375rem;
  }

  .edit-button,
  .delete-button {
    width: 100%;
    box-sizing: border-box;
  }
}
</style>