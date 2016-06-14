from django.contrib import admin

from .models import SliderItem, SliderItemLink, Image

# Register your models here.
admin.site.register(Image)
admin.site.register(SliderItem)
admin.site.register(SliderItemLink)
