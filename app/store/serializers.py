from store.models import Clothes, CartItem
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError


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

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise ValidationError("A user with that username already exists.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
