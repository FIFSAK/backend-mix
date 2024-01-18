from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
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
        fields = ("username", "password",)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            # Hash the password
            password=make_password(validated_data['password'])
        )
        user.save()
        return user


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
