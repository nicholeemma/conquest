from django.contrib import admin

# Register your models here.
from . import models
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name",  "description", "picture")

admin.site.register(models.Item, ItemAdmin)