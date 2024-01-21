from django.db import models

# Create your models here.


class   Shop(models.Model):
    title=models.CharField(max_length=225,blank=False)
    description=models.CharField(max_length=225,blank=False)
    front_image=models.ImageField(upload_to='media/shop_now_home_front/%Y%m%d/',blank=False)
    back_image=models.ImageField(upload_to='media/shop_now_home_back/%Y%m%d/',blank=False)
    button_text=models.CharField(max_length=225,blank=False)

    def __str__(self):
        return self.title
    

class   Shop_now(models.Model):
    product_name=models.CharField(max_length=225,blank=False)
    description=models.CharField(max_length=2000,blank=False)
    image=models.ImageField(upload_to='media/products/%Y%m%d/',blank=False)
    price=models.CharField(max_length=225,blank=False)
    
    def __str__(self):
        return self.product_name    
    

