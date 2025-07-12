INSTALLED_APPS = [
    ...
    'properties',
    'django_redis',
]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",  # use "redis://redis:6379/1" if Django runs in a container
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
