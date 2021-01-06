from django.urls import path
from .views import TaskListCreate, CreateProject, ListUserProjects
urlpatterns = [
    path('tasks/', TaskListCreate.as_view()),
    path('create-project/', CreateProject.as_view()),
    path('my-projects/', ListUserProjects.as_view()),
]
