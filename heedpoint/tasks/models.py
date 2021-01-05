from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

PRIORITY_VALUES = (
    ('f', 'Important and Urgent'),
    ('l', 'Important not Urgent'),
    ('d', 'Delegate'),
    ('e', 'Eliminate'),
    ('n', 'Not Set'),
)

STATUS_VALUES = (
    ('h', 'Holding'),
    ('p', 'Prioritized'),
    ('s', 'Started'),
    ('f', 'Finished'),
)


class User(AbstractUser):
    pass


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(
        max_length=100, help_text="Enter the title of the Task")
    description = models.CharField(
        max_length=500, help_text="Enter the description of the task")
    timestamp = models.DateTimeField(auto_now_add=True)
    time_needed = models.DurationField(null=True, blank=True)
    time_spent = models.DurationField(null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_VALUES,
        blank=True,
        default='h',
        help_text='Task Status'
    )
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_VALUES,
        blank=True,
        default='n',
        help_text='Priority Status'
    )

    def __str__(self):
        return self.title


class Project(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="owned")
    managers = models.ManyToManyField(
        User, blank=True, null=True, related_name='managing')
    developers = models.ManyToManyField(
        User, blank=True, null=True, related_name="projects")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    dead_line = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
