from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("experiences/", api_views.project_list, name="project-list"),
    path("experiences/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
]