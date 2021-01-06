from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Task, Project
from .serializers import TaskSerializer, CreateProjectSerializer, ProjectSerializer


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateProject(APIView):
    serializer_class = CreateProjectSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            title = serializer.data.get('title')
            description = serializer.data.get('description')
            dead_line = serializer.data.get('dead_line')
        project = Project(owner=user, title=title,
                          description=description, dead_line=dead_line)
        project.save()
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)


class ListUserProjects(generics.ListAPIView):
    def get_queryset(self):
        user = self.request.user
        return user.owned.all()
    serializer_class = ProjectSerializer
