from django.db import models
from django.contrib.auth.models import User


class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    learning_objectives = models.TextField()

    def __str__(self):
        return self.title


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ['user', 'module']