from django.contrib import admin
from properties.models import Property
# Register your models here.

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "street",
        "city",
        "owner",
    )
