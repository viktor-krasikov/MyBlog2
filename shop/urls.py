from django.urls import path

from .views import shop, ProductListView, ProductDetailView

urlpatterns = [
    path('', shop, name='shop'),
    path('products/', ProductListView.as_view(), name='post_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='post_detail'),
]
