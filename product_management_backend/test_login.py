import sys
import os
import requests
from django.contrib.auth.hashers import check_password

# 设置Django环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_management_backend.settings')

# 导入Django并初始化
import django
django.setup()

from django.contrib.auth.models import User

# 检查用户信息并重置密码
def check_and_reset_user(username, new_password):
    try:
        user = User.objects.get(username=username)
        print(f"找到用户: {username}")
        print(f"邮箱: {user.email}")
        print(f"是否为管理员: {user.is_staff}")
        print(f"是否为超级用户: {user.is_superuser}")
        print(f"账户是否活跃: {user.is_active}")
        print(f"密码哈希: {user.password}")

        # 检查密码是否匹配
        is_password_correct = check_password('admin123', user.password)
        print(f"密码 'admin123' 是否匹配: {is_password_correct}")

        # 重置密码
        user.set_password(new_password)
        user.save()
        print(f"密码已重置为: {new_password}")
        return True
    except User.DoesNotExist:
        print(f"用户 {username} 不存在")
        return False

# 测试登录函数
def test_login(username, password):
    url = 'http://localhost:8000/api/admin-login/'
    data = {
        'username': username,
        'password': password
    }

    try:
        print(f"尝试登录用户: {username}")
        response = requests.post(url, json=data)
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.json()}")

        if response.status_code == 200:
            print("登录成功!")
        else:
            print("登录失败!")
    except Exception as e:
        print(f"请求发生错误: {str(e)}")

if __name__ == '__main__':
    # 检查并重置admin用户密码
    check_and_reset_user('admin', 'admin123')
    # 再次测试登录
    test_login('admin', 'admin123')