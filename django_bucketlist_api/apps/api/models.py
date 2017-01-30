from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Task(models.Model):

    objective = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    # Return the objective in string form. for py2
    def __str__(self):
        return self.objective

    # Return the objective in string form. for py3
    def __unicode__(self):
        return self.objective
        
