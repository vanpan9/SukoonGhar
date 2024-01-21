from django.contrib import admin
from .models import Aboutus,Objectives,Event,Team,Post,SGPeople, Gallery
from django.utils.html import format_html

# Register your models here.
class AboutusAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" '.format(object.image.url))


    list_display=('id','myphoto','main_title')
    list_display_links=("main_title",'myphoto',)

class PeopleAdmin(admin.ModelAdmin):
   def myphoto(self,object):
        return format_html('<img src="{}" width="40" '.format(object.image.url))


   list_display=('id','name','image')
   list_display_links=("name",'image',)

class GalleryAdmin(admin.ModelAdmin):
   def myphoto(self,object):
        return format_html('<img src="{}" width="40" '.format(object.image.url))


   list_display=('id','name','image')
   list_display_links=("name",'image',)


admin.site.register(Aboutus,AboutusAdmin)
admin.site.register(Objectives)
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Post)
admin.site.register(Gallery,GalleryAdmin)

admin.site.register(SGPeople,PeopleAdmin)



