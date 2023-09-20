from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(floors)
admin.site.register(occupants)
admin.site.register(locations)
admin.site.register(electricities)
