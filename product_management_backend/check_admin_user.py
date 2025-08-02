import sys
import os

# 设置Django环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_management_backend.settings')

# 导入Django并初始化
import django
django.setup()

from django.contrib.auth.models import User

# 检查admin用户
try:
    user = User.objects.get(username='admin')
    print(f'用户名: {user.username}')
    print(f'邮箱: {user.email}')
    print(f'是否为管理员: {user.is_staff}')
    print(f'是否为超级用户: {user.is_superuser}')
    print(f'账户是否活跃: {user.is_active}')
except User.DoesNotExist:
    print('admin用户不存在')