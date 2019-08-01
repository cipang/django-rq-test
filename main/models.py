from django.db import models


class T(models.Model):
    created = models.DateTimeField()
    value = models.TextField()
    modified = models.DateTimeField(null=True, default=None, blank=True)
