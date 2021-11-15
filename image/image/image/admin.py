from django.contrib import admin
from . import models


@admin.register(models.Good)
class GoodAdmin(admin.ModelAdmin):
	list_display = ['description_text', 'price_text', 'image_sale', 'id']

