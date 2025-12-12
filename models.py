from django.db import models

# Create your models here.
class lcategory(models.Model):
    category=models.CharField(max_length=50,null=True)
    cpic=models.ImageField(upload_to="static/category/",null=True)
    def __str__(self):
        return self.category
    

class mentor(models.Model):
    name=models.CharField(max_length=50,null=True)
    picture=models.ImageField(upload_to="static/mentor/",null=True)
    qualification=models.CharField(max_length=40,null=True)
    mabout=models.TextField(null=True)
    experience=models.CharField(max_length=40,null=True)
    def __str__(self):
        return self.name
class contactus(models.Model):
    name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=40,null=True)
    message=models.TextField(null=True)
class igallery(models.Model):
    picture=models.ImageField(upload_to="static/gallery/",null=True)
    title=models.CharField(max_length=50,null=True)

class lecture(models.Model):
      title=models.CharField(max_length=50,null=True)
      vlink=models.CharField(max_length=100,null=True)
      description=models.TextField(null=True)
      mentor=models.ForeignKey(mentor,on_delete=models.CASCADE)
      category=models.ForeignKey(lcategory,on_delete=models.CASCADE)
      added_date=models.DateField(null=True)

