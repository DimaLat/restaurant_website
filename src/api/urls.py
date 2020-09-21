from django.urls import path

from ..api import api_views
from .api_views import CategoryAPIView

urlpatterns = [

    path('categories/<str:id>', CategoryAPIView.as_view(), name='categories'),
    path('products/', api_views.product_list, name='products_list'),
    path('products/<str:pk>/', api_views.product_detail, name='products_detail'),

]
