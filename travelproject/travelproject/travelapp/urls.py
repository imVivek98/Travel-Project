
from django.urls import path

from travelproject import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.demo,name="demo"),
   # path('about/',views.about,name="about"),
   # path('contact/',views.contact,name="contact")
   #  path('add/',views.addition,name="addition")


]

