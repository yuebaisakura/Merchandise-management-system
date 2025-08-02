import sys
import os

# 设置Django环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_management_backend.settings')

def create_superuser():
    # 导入Django并初始化
    import django
    django.setup()

    from django.contrib.auth.models import User

    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f'Superuser {username} created successfully')
    else:
        print(f'Superuser {username} already exists')

if __name__ == '__main__':
    create_superuser()