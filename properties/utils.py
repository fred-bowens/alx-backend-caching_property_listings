import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)  # Get Django's logger for this module

def get_all_properties():
    """
    Get all properties, using Redis cache to reduce DB hits.
    Cache timeout is 1 hour (3600 seconds).
    """

    # Try to fetch cached data
    properties = cache.get('all_properties')

    if properties is None:
        # If not in cache, query the database
        queryset = Property.objects.all().values()  # Get all properties as dicts
        properties = list(queryset)  # Convert queryset to list of dictionaries

        # Store in Redis with 1-hour expiration (3600 seconds)
        cache.set('all_properties', properties, timeout=3600)

    return properties

def get_redis_cache_metrics():
    """
    Retrieve Redis cache hit/miss metrics and calculate the hit ratio.
    """

    # Get the default Redis connection used by Django
    redis_conn = get_redis_connection("default")

    # Run the INFO command to get internal Redis stats
    info = redis_conn.info()

    # Extract hits and misses
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    # Avoid division by zero
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else None

    # Log the metrics
    logger.info(f"Redis Metrics - Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio}")

    # Return results in dictionary form
    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio
    }
