from django.contrib import admin
from .models  import *

# Register your models here.
class lcategoryAdmin(admin.ModelAdmin):
    list_display=('category','cpic')
     
admin.site.register(lcategory,lcategoryAdmin)

class mentorAdmin(admin.ModelAdmin):
    list_display=('name','picture','qualification','mabout','experience')

admin.site.register(mentor,mentorAdmin)  

class contactusAdmin(admin.ModelAdmin):
    list_display=('name','mobile','email','message')

admin.site.register(contactus,contactusAdmin)

class igallerAdmin(admin.ModelAdmin):
    list_display=('picture','title')
    
admin.site.register(igallery,igallerAdmin)

class lectureAdmin(admin.ModelAdmin):
    list_display=("title","vlink","description","mentor","category")
    
admin.site.register(lecture,lectureAdmin)





