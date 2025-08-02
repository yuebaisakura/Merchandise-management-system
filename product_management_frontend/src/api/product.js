import axios from 'axios';

// 创建Axios实例
const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
  headers: {
    'Content-Type': 'application/json'
  }
});

// 请求拦截器 - 添加认证token
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Token ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// 商品API
export const productAPI = {
  // 获取所有商品
  getAllProducts: () => api.get('products/'),
  // 获取单个商品
  getProductById: (id) => api.get(`products/${id}/`),
  // 创建商品
  createProduct: (productData) => api.post('products/', productData),
  // 更新商品
  updateProduct: (id, productData) => api.put(`products/${id}/`, productData),
  // 部分更新商品
  partialUpdateProduct: (id, productData) => api.patch(`products/${id}/`, productData),
  // 删除商品
  deleteProduct: (id) => api.delete(`products/${id}/`)
};

// 管理员API
export const adminAPI = {
  // 管理员登录
  login: (credentials) => api.post('admin-login/', credentials)
};

export default api;