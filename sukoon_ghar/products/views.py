from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Shop_now

# Create your views here.


   
def show_item(request,id):
    product_info = get_object_or_404(Shop_now,pk=id)
    data={
        'product_info':product_info,
    }
    product=request.POST.get('product')
    print(product)
    return render(request,'products/product_details.html',data)
def post(self,request):
     pass
@login_required(login_url='register')
def cart(request):
  
  return render(request,'products/cart.html')