from django.contrib import admin
from .models import Paparazzo, Pic, Category, tags, Location
# Register your models here.
class PicAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Pic, PicAdmin)
admin.site.register(Paparazzo)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(tags)