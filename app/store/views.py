import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response

from .models import *
from rest_framework import viewsets, filters, permissions, status
from .serializers import ClothesSerializer, UserSerializer, CartItemSerializer
from django.contrib.auth.models import User


# def clothes_view(request, type):
#     """
#     Returns a list of clothes objects in JSON format based on the type.
#     Only responds to HTTP GET requests.
#     """
#     if request.method != "GET":
#         return HttpResponse("Method not allowed", status=405)
#
#     model_map = {
#         'Trousers': Trousers,
#         'TShirtsAndTops': TShirtsAndTops,
#         'Jacket': Jacket,
#         'ShirtsAndBlouses': ShirtsAndBlouses,
#         'Dresses': Dresses,
#         'OverallsJacketsRaincoatsCardigans': OverallsJacketsRaincoatsCardigans,
#         'PantsuitsShortsSkirts': PantsuitsShortsSkirts,
#         'Jeans': Jeans,
#         'Underwear': Underwear,
#     }
#
#     model = model_map.get(type)
#     if not model:
#         return HttpResponse("Invalid type", status=400)
#
#     object_query_set = model.objects.all()
#     data = serialize('json', object_query_set)
#     data = json.loads(data)
#     return JsonResponse(data, safe=False)


class ClothesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing clothes.
    """

    queryset = Clothes.objects.all()

    serializer_class = ClothesSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', '=vendor_code', '=sizes__size', 'type_category__category_name']
    ordering_fields = ['price']


class UserView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all();

    serializer_class = UserSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def create(self, *args, **kwargs):
        # Create a mutable copy of request.data
        data = self.request.data.copy()
        clothes_id = data.get('clothes')
        try:
            clothes = Clothes.objects.get(id=clothes_id)
        except Clothes.DoesNotExist:
            raise NotFound('Товар (одежда) с указанным ID не найден.')

        existing_item = CartItem.objects.filter(
            user=self.request.user, clothes=clothes
        ).first()

        # Pass the user's primary key (pk) to the serializer
        data['user'] = self.request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        if existing_item:
            existing_item.quantity += 1
            existing_item.save(update_fields=['quantity'])
        else:
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            # Проверка, принадлежит ли объект корзины текущему пользователю
            raise PermissionDenied("Вы не можете удалить этот элемент корзины.")
        if instance.quantity > 1:
            instance.quantity -= 1
            instance.save(update_fields=['quantity'])
        else:
            instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
