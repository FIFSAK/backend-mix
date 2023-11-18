from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *



def trousers_view(request):
    if request.method == "GET":
        objectQuerySet = Trousers.objects.all()
        data = serialize('json', list(objectQuerySet))
        return JsonResponse(data, safe=False)
    return HttpResponse(status=400)
