from django.db import models

# Create your models here.

class   Aboutus(models.Model):
    main_title=models.CharField(max_length=225,blank=False)
    main_description=models.CharField(max_length=225,blank=False)
    image=models.ImageField(upload_to='media/aboutus/%Y%m%d/',blank=False)
    sub_title=models.CharField(max_length=225,blank=False)
    sub_description=models.CharField(max_length=225,blank=False)    

    def __str__(self):
        return self.main_title



class   Objectives(models.Model):
    icon_choices=(
        ("bi bi-puzzle","Skill Diversification"),
        ("bi bi-emoji-smile","Mental Health Support"),
        ("bi bi-laptop","Digital Literacy"),
        ("bi bi-people","Parenting Workshops"),
        ("bi bi-cash","Financial Literacy"),
        ("bi bi-heart","Health and Nutrition"),
        ("bi bi-chat-square","Community Engagement"),
        ("bi bi-palette","Art and Expression"),
        ("bi bi-book","Education Empowerment"),
    )

    title_choices=(
        ("Skill Diversification","Skill Diversification"),
        ("Mental Health Support","Mental Health Support"),
        ("Digital Literacy","Digital Literacy"),
        ("Parenting Workshops","Parenting Workshops"),
        ("Financial Literacy","Financial Literacy"),
        ("Health and Nutrition","Health and Nutrition"),
        ("Community Engagement","Community Engagement"),
        ("Art and Expression","Art and Expression"),
        ("Education Empowerment","Education Empowerment"),
    )
    title=models.CharField(choices=title_choices,max_length=225,blank=False)
    description=models.CharField(max_length=225,blank=False)
    icon=models.CharField(choices=icon_choices,max_length=225,blank=False)
   
    def __str__(self):
        return self.title
    
class Event(models.Model):
    event_name=models.CharField(max_length=225,blank=False)
    event_description=models.CharField(max_length=225,blank=False)
    image=models.ImageField(upload_to='media/events/%Y%m%d/',blank=False)
    
       
    def __str__(self):
        return self.event_name
    
  
class Team(models.Model):
    name=models.CharField(max_length=225,blank=False)
    role=models.CharField(max_length=225,blank=False)
    description=models.CharField(max_length=225,blank=False)
    image=models.ImageField(upload_to='media/team/%Y%m%d/',blank=False)
    fb_link=models.CharField(max_length=225,blank=False)
    insta_link=models.CharField(max_length=225,blank=False)
     
    def __str__(self):
        return self.name
    
  
class Post(models.Model):
    title= models.CharField(max_length=225,blank=False)
    description= models.CharField(max_length=225,blank=False)
    post_link= models.CharField(max_length=225,blank=False)
    post_image= models.ImageField(upload_to='media/team/%Y%m%d/',blank=False)
    def __str__(self):
        return self.title    
    

    
class SGPeople(models.Model):
    name= models.CharField(max_length=225,blank=False)
    image= models.ImageField(upload_to='media/people/%Y%m%d/',blank=False)
    role=models.CharField(max_length=225,blank=False)

    description= models.CharField(max_length=225,blank=False)

    

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    name= models.CharField(max_length=225,blank=False)
    image= models.ImageField(upload_to='media/people/%Y%m%d/',blank=False)

    description= models.CharField(max_length=225,blank=False)



    def __str__(self):
     return self.name