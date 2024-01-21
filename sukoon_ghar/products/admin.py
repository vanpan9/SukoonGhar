from django.contrib import admin
from .models import Shop, Shop_now
from django.utils.html import format_html

# Register your models here.

class Shop_nowAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" '.format(object.image.url))


    list_display=('id','myphoto','product_name')
    list_display_links=("product_name",'myphoto',)


admin.site.register(Shop)
admin.site.register(Shop_now,Shop_nowAdmin)