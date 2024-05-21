
from django.urls import path
from product_management.views import ProductListView, ProductDetailView
from user_management.views import UserRegistrationView, UserAuthenticationView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserAuthenticationView.as_view(), name='user-login'),
]
