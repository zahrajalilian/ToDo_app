from django.db import models
from django.urls import reverse
import datetime
from django.db.models import Count
#
time_now = datetime.datetime.now()

"""
global scope
"""


class CategoriesManager(models.Manager):
    """
     a manager to manage our category full or empty
    """
    def empty(self):
        return self.annotate(c=Count('category')).filter(c=0)

    def full(self):
        return self.annotate(c=Count('category')).filter(c__gt=0)



class ManageTime(models.Manager):
    """
     a manager to manage our out dated tasks
    """
    def get_queryset(self):
        return super().get_queryset().filter(due_date_time__lt=time_now)


class ToDo(models.Model):
    """
    our todo model with diffrent fields

    """
    PRIORITY = [('HIGH', 'HIGH'), ('MIDDLE', 'MIDDLE'), ('LOW', 'LOW')]

    CHOICES_FULL = [('Education', 'Education'), ('sports ', 'sports'),
                    ('ToBuy', 'ToBuy'), ('House Chores', 'House Chores'),
                    ('Django Project', 'Django Project'), ('undecided', 'undecided')]
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(choices=PRIORITY, max_length=200, default='LOW')
    due_date_time = models.DateTimeField()
    category = models.CharField(choices=CHOICES_FULL, max_length=100, default='undecided')
    objects= models.Manager()
    time_manager = ManageTime()
    categoryManager = CategoriesManager()

    class Meta:
        ordering = ['-due_date_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
