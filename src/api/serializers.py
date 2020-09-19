from rest_framework import serializers

from ..restaurant.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category  # указываем что модель будет использоваться категория, а дальше какие поля используем
        fields = [
            'id', 'name', 'slug'
        ]


class BaseProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    name = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image_width = serializers.IntegerField(required=True)
    image_height = serializers.IntegerField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=0,required=True)
    stock = serializers.IntegerField()
    available = serializers.BooleanField(required=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Product
        fields = '__all__'
