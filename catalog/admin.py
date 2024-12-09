from django.contrib import admin
from .models import Neighborhood, PropertyType, PriceRange, Photo, Property, SearchLog, Events

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(PropertyType)
admin.site.register(PriceRange)
admin.site.register(Photo)
admin.site.register(Property)
admin.site.register(SearchLog)
admin.site.register(Events)
