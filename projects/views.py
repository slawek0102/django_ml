from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return render(request, 'projects.html')

def project(request, project_id):
    return render(request, 'single-project.html', {'project': project_id})
def home(request):
    msg ='Home Page w Django ze stylowaniem bootstrap'
    return render(request, 'home.html', {'message': msg})