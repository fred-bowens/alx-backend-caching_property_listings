from django.core.cache import cache
from .models import Property

def get_all_properties():
    # Try to get cached data
    properties = cache.get('all_properties')  
    
    if properties is None:
        # If not cached, query the database
        properties = list(Property.objects.all().values())  # Convert queryset to list of dicts

        # Cache the result for 1 hour (3600 seconds)
        cache.set('all_properties', properties, timeout=3600)

    return properties
