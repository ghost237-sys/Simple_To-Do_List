from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todolist',null=True)
    name = models.TextField(max_length=200,unique=True)


    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    Text = models.TextField(max_length=200)
    Complete = models.BooleanField(default=False)

    def __str__(self):
        return self.Text



