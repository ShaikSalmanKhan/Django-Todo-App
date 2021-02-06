from django.db import models


# Create your models here.
class Todo(models.Model):
    todo_name       =  models.CharField(max_length=20)
    todo_completed  =  models.BooleanField(default=False)
    todo_created    =  models.DateTimeField(auto_now_add=True)
