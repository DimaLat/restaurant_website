from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, BaseProductSerializer
from ..restaurant.models import Category, Product


class CategoryPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 10


class ProductPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 20


class CategoryAPIView(ListCreateAPIView,
                          RetrieveUpdateAPIView):  # ListAPIView - для просмотра ListCreateAPIView еще и для
    # создания и изменения
    serializer_class = CategorySerializer  # указываем какой используем сериалайзер
    pagination_class = CategoryPagination  # указываем класс пагинации
    queryset = Category.objects.all()
    lookup_field = "id"


class ProductListCreateAPIView(ListCreateAPIView, RetrieveUpdateAPIView):
    serializer_class = BaseProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    filter_backends = [SearchFilter]
    search_fields = ['price']  # за поиском прописываем в адресную строку http://127.0.0.1:8000/api/products/?search=10


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = BaseProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
