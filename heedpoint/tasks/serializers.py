from rest_framework import serializers
from .models import Task, Project


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title']


class ProjectSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_user_name')
    managers = serializers.SerializerMethodField('get_managers')
    developers = serializers.SerializerMethodField('get_developers')

    class Meta:
        model = Project
        fields = ['id', 'owner', 'username',
                  'title', 'managers', 'developers', 'description', 'dead_line']

    def get_user_name(self, obj):
        return(obj.owner.username)

    def get_managers(self, obj):
        return(manager.username for manager in obj.managers.all())

    def get_developers(self, obj):
        return(developer.username for developer in obj.developers.all())


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'dead_line']
