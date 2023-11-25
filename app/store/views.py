import json
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound

from .models import *
from rest_framework import viewsets, filters
from .serializers import TrousersSerializer


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
    def get_queryset(self):
        type_map = {
            'Trousers': Trousers,
            'TShirtsAndTops': TShirtsAndTops,
            'Jacket': Jacket,
            'ShirtsAndBlouses': ShirtsAndBlouses,
            'Dresses': Dresses,
            'OverallsJacketsRaincoatsCardigans': OverallsJacketsRaincoatsCardigans,
            'PantsuitsShortsSkirts': PantsuitsShortsSkirts,
            'Jeans': Jeans,
            'Underwear': Underwear,
        }
        model = type_map.get(self.request.GET.get("type"))
        if not model:
            raise NotFound(detail="Incorrect type", code=404)
        return model.objects.all()

    serializer_class = TrousersSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', '=vendore_code', '=sizes']
    ordering_fields = ['price']



