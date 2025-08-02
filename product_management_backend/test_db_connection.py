import sys
import os

# 设置Django环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_management_backend.settings')

# 导入Django并初始化
import django
django.setup()

from django.db import connection

try:
    # 尝试连接数据库
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"数据库连接成功! 测试结果: {result}")
except Exception as e:
    print(f"数据库连接失败: {str(e)}")