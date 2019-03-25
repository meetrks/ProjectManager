from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel
from project.models import Project


class Task(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField()
    assignee = models.ForeignKey(User, related_name="task_assignee", on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('created',)
