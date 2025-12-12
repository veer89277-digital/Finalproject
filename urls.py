from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("home/",views.index),
    path("contact/",views.contact),
    path("gallery/",views.gallery),
    path("wchoose/",views.wchoose),
    path("team/",views.team),
    path("video/",views.video),
    path("category/",views.mycategory),
    path("aboutus/",views.aboutus),
]