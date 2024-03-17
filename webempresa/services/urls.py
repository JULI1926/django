from django.urls import path
from . import views

urlpatterns = [
    #App core
    path('',views.services, name="service"),    
]
