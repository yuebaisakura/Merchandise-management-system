import { createRouter, createWebHistory } from 'vue-router';
import AdminLogin from '../components/Admin/Login.vue';
import ProductList from '../components/Products/ProductList.vue';
import ProductForm from '../components/Products/ProductForm.vue';

// 路由守卫，检查是否已登录
function requireAuth(to, from, next) {
  const token = localStorage.getItem('token');
  if (!token) {
    next({ path: '/login' });
  } else {
    next();
  }
}

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: AdminLogin
  },
  {
    path: '/products',
    name: 'ProductList',
    component: ProductList,
    beforeEnter: requireAuth
  },
  {
    path: '/products/add',
    name: 'AddProduct',
    component: ProductForm,
    beforeEnter: requireAuth
  },
  {
    path: '/products/edit/:id',
    name: 'EditProduct',
    component: ProductForm,
    beforeEnter: requireAuth,
    props: true
  },
  // 默认路由重定向到登录页
  {
    path: '/',
    redirect: '/login'
  },
  // 404页面
  {
    path: '/:catchAll(.*)',
    redirect: '/login'
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;