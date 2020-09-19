from django.urls import path

from .api_views import CategoryAPIView, ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [

    path('categories/<str:id>', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductListCreateAPIView.as_view(), name='products_list'),
    path('products/<str:id>/', ProductDetailAPIView.as_view(), name='products_detail'),

]
