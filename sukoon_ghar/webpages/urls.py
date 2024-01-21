from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('events',views.events,name='events'),
    path('donate',views.donate,name='donate'),
    path('items',views.items,name="items")
  



]