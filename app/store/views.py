import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from .models import Trousers

def trousers_view(request):
    """
    Returns a list of all Trousers objects in JSON format.
    Only responds to HTTP GET requests.
    """
    if request.method == "GET":
        objectQuerySet = Trousers.objects.all()
        data = serialize('json', objectQuerySet)  # Directly pass the queryset
        data = json.loads(data)
        return JsonResponse(data, safe=False)  # For an array of JSON objects
    else:
        return HttpResponse("Method not allowed", status=405)  # Method Not Allowed status
