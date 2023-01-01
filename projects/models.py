from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


status = (
    ('1', 'Stuck'),
    ('2', 'Working'),
    ('3', 'Done'),
)

due = (
    ('1', 'On Due'),
    ('2', 'Overdue'),
    ('3', 'Done'),
)

# Create your models here.



class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assign = models.ManyToManyField(User)
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=1)
    due = models.CharField(max_length=7, choices=due, default=1)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return(self.task_name)