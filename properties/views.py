from django.http import JsonResponse
from .utils import get_all_properties  # Import your caching function
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    """
    Returns all property listings as JSON.
    The entire response is cached in Redis for 15 minutes.
    """
    properties = Property.objects.all().values()  # Query all properties from the database
    data = list(properties)  # Convert the queryset to a list of dictionaries
    return JsonResponse(data, safe=False)  # Return as JSON response
