from django.db import models


class Todo(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
