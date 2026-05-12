from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    caution = models.TextField(blank=True)
    preparation = models.TextField(blank=True)
    detail = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title