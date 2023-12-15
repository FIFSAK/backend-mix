from django.contrib.auth.models import User
from rest_framework import serializers

from store.models import Clothes, CartItem

class ClothesSerializer(serializers.ModelSerializer):
    type_category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='category_name'
    )
    sizes = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='size'
    )

    class Meta:
        model = Clothes
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
