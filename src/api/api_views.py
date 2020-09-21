from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, BaseProductSerializer
from ..restaurant.models import Category, Product


class CategoryPagination(PageNumberPagination):
    page_size = 3
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


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all code Products, or create a new Product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = BaseProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BaseProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code product.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BaseProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BaseProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
