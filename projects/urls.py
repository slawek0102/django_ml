from django.urls import path
from projects.views import projects, project, home


urlpatterns =  [
    # path("home/", getHomePage),
    path("projects/", projects, name="projects"),
    path("project/<str:project_id>/", project, name="project"),
    path("", home)
]