from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, AdminLoginView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
]