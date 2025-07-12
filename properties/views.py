from django.http import JsonResponse
from .utils import get_all_properties  # Import your caching function

def property_list(request):
    """
    Return all properties from cache or DB.
    """
    data = get_all_properties()  # Use the cached or fresh queryset
    return JsonResponse(data, safe=False) 
