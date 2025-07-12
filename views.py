from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property
from django.utils.decorators import method_decorator
from django.views import View

# Cache this view's response for 15 minutes (60 * 15 = 900 seconds)
@cache_page(60 * 15)
def property_list(request):
    """
    Return a JSON response with all properties.
    This response is cached in Redis for 15 minutes.
    """
    properties = Property.objects.all().values()  
    data = list(properties)  
    return JsonResponse(data, safe=False) 
