from django.urls import path
from . import views     

urlpatterns = [
    path('',views.home, name="home"),
    path('services/',views.services, name="services"),
    path('visit/',views.visit, name="visit"),
    path('contact/',views.contact, name="contact"),
    path('blog/',views.blog, name="blog"),
    path('history/',views.contact, name="history"),
    path('other/',views.contact, name="other"),
]