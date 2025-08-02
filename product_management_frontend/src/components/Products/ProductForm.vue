<template>
  <div class="products-container">
    <h2 class="page-title">{{ isEditing ? '编辑商品' : '添加商品' }}</h2>
    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="error" class="error-message">{{ error }}</div>
    <form v-else @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">商品名称</label>
        <input
          type="text"
          id="name"
          v-model="product.name"
          placeholder="请输入商品名称"
          required
        >
      </div>
      <div class="form-group">
        <label for="description">商品描述</label>
        <textarea
          id="description"
          v-model="product.description"
          placeholder="请输入商品描述"
          rows="4"
        ></textarea>
      </div>
      <div class="form-group">
        <label for="price">商品价格</label>
        <input
          type="number"
          id="price"
          v-model="product.price"
          placeholder="请输入商品价格"
          step="0.01"
          min="0"
          required
        >
      </div>
      <div class="form-group">
        <label for="stock">商品库存</label>
        <input
          type="number"
          id="stock"
          v-model="product.stock"
          placeholder="请输入商品库存"
          min="0"
          required
        >
      </div>
      <div class="form-actions">
        <button type="button" @click="$router.go(-1)" class="cancel-button">取消</button>
        <button type="submit" class="submit-button">{{ isEditing ? '更新' : '添加' }}</button>
      </div>
    </form>
  </div>
</template>

<script>
import { productAPI } from '../../api/product';


export default {
  name: 'ProductForm',
  props: {
    productId: { type: String, default: null }
  },
  data() {
    return {
      product: {
        name: '',
        description: '',
        price: '',
        stock: ''
      },
      isEditing: false,
      loading: true,
      error: ''
    };
  },
  mounted() {
    if (this.productId) {
      this.isEditing = true;
      this.fetchProductDetails();
    } else {
      this.loading = false;
    }
  },
  methods: {
    async fetchProductDetails() {
      try {
        this.loading = true;
        this.error = '';
        const response = await productAPI.getProductById(this.productId);
        this.product = response.data;
      } catch (err) {
        this.error = err.response?.data?.detail || '获取商品详情失败';
      } finally {
        this.loading = false;
      }
    },
    async handleSubmit() {
      try {
        this.error = '';
        if (this.isEditing) {
          await productAPI.updateProduct(this.productId, this.product);
        } else {
          await productAPI.createProduct(this.product);
        }
        // 提交成功后返回商品列表页
        this.$router.push('/products');
      } catch (err) {
        this.error = err.response?.data?.detail || (this.isEditing ? '更新商品失败' : '添加商品失败');
      }
    }
  }
};
</script>

<style scoped>
.products-container {
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

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  color: #555;
  font-weight: 500;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-group textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  margin-top: 30px;
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.cancel-button {
  background-color: #f1f1f1;
  color: #333;
  border: none;
  border-radius: 4px;
  padding: 10px 16px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.cancel-button:hover {
  background-color: #e0e0e0;
}

.submit-button {
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 16px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #3aa876;
}

input:focus, textarea:focus {
  border-color: #3498db;
  box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
  outline: none;
}

/* 响应式表单调整 */
@media (max-width: 768px) {
  .page-title {
    font-size: 1.5rem;
  }

  .form-group input,
  .form-group textarea {
    padding: 0.75rem;
    font-size: 1rem;
  }

  .form-actions {
    flex-direction: column;
    gap: 0.5rem;
  }

  .cancel-button,
  .submit-button {
    width: 100%;
    padding: 0.75rem;
    box-sizing: border-box;
  }
}

@media (max-width: 480px) {
  .page-title {
    font-size: 1.25rem;
  }

  .form-group {
    margin-bottom: 1rem;
  }
}
</style>  form {
    padding: 20px;
  }

  .btn {
    padding: 10px 16px;
    font-size: 14px;
  }
}

@media (max-width: 480px) {
  .btn {
    padding: 8px 12px;
    font-size: 13px;
  }

  .btn-icon {
    width: 14px;
    height: 14px;
  }
}
