from . import views
from django.urls import path

urlpatterns=[
    path('<int:id>',views.show_item,name="show_item"),
    path('cart',views.cart,name='cart'),




]