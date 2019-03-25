from django.contrib.auth.models import User
from django.db import models

from base.models import BaseModel


class Project(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)
    owner = models.ForeignKey(User, related_name="project_owner", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('created',)
