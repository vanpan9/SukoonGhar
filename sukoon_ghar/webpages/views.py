
from django.shortcuts import render
from .models import Aboutus,Objectives,Event,Team,Post,SGPeople, Gallery
from products.models import Shop,Shop_now
# Create your views here.

def home(request):
 about_data=Aboutus.objects.all()[0]
 objectives_data=Objectives.objects.all()
 shop_img=Shop.objects.all()[0]
 event_data=Event.objects.all()
 team_data=Team.objects.all()
 post_data=Post.objects.all()
 data={
  'about_data':about_data,
  'objectives_data':objectives_data,
  "shop_img":shop_img,
  'event_data':event_data,
  'team_data':team_data,
  'post_data':post_data,

 }
 return render(request,'webpages/home.html',data)

def about(request):
 people_data=SGPeople.objects.all()
 data={
  'people_data':people_data,
 }
 return render(request,'webpages/about.html',data)



def items(request):
 items_data=Shop_now.objects.all()
 data={
  'items_data':items_data,
 }
 return render(request,'products/shop_now.html',data)


def events(request):
 event_data=Event.objects.all()
 gallery_data=Gallery.objects.all()
 data={
  'event_data':event_data,
  'gallery_data':gallery_data
 }
 return render(request,'webpages/events.html',data)

def donate(request):
 return render(request,'webpages/donate.html')



 