from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Task(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
