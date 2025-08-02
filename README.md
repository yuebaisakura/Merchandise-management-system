# 商品管理系统

## 项目简介
这是一个完整的商品管理系统，包含后端API和前端界面。系统提供商品的添加、编辑、删除和查询功能，以及用户登录认证。

## 技术栈

### 后端
- Python 3.8+
- Django 4.2+
- Django REST framework
- SQLite (默认) / MySQL

### 前端
- Vue 3
- Vite
- Axios
- Vue Router

## 项目结构
```
商品管理系统/
├── product_management_backend/  # 后端Django项目
│   ├── product_management_backend/  # 项目配置
│   ├── products/  # 商品应用
│   ├── manage.py  # Django管理脚本
│   └── ...
└── product_management_frontend/  # 前端Vue项目
    ├── src/  # 源代码
    ├── index.html  # 入口HTML
    ├── package.json  # 依赖配置
    └── ...
```

## 安装说明

### 后端安装
1. 进入后端目录
```bash
cd product_management_backend
```

2. 创建虚拟环境
```bash
python -m venv venv
```

3. 激活虚拟环境
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. 安装依赖
```bash
pip install -r requirements.txt
```

5. 迁移数据库
```bash
python manage.py makemigrations
python manage.py migrate
```

6. 创建超级用户
```bash
python manage.py createsuperuser
```

7. 启动后端服务器
```bash
python manage.py runserver
```

### 前端安装
1. 进入前端目录
```bash
cd product_management_frontend
```

2. 安装依赖
```bash
npm install
```

3. 启动前端开发服务器
```bash
npm run dev
```

## 使用方法
1. 确保后端服务器和前端服务器都已启动
2. 访问前端页面: http://localhost:5173
3. 使用创建的超级用户账号登录
4. 开始管理商品

## 功能特点
- 用户登录认证
- 商品列表展示
- 商品添加、编辑和删除
- 响应式布局，适配不同设备

## 项目截图
(可在此处添加项目截图)

## 联系方式
如有问题或建议，请联系: [tongmeiyuebai667@gmail.com]