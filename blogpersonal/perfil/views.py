from django.shortcuts import render, HttpResponse

#Models
from .models import Project

# Create your views here.

def profile(requests):
    """
    p1 = Project(title = "Curso de HTML", desc = "Descripción de HTML")
    p1.save()

    p2 = Project(title = "Curso de CSS", desc = "Descripción de CSS")
    p2.save()

    p3 = Project(title = "Curso de Django", desc = "Descripción de Django")
    p3.save()
    """

    projects = Project.objects.all()
    return HttpResponse(projects)
