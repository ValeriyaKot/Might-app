from django.utils import timezone
from django.db import models
from rest_framework.exceptions import ValidationError


class Badge(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    picture = models.ImageField()
    group = models.ForeignKey('GroupBadges', related_name='badges', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class EmployeeBadge(models.Model):
    isAnonymous = models.BooleanField(default=False)
    employee_guid = models.CharField(max_length=40)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)
    giver_guid = models.CharField(max_length=40)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created']

    def clean(self):
        if self.employee_guid == self.giver_guid:
            raise ValidationError("Employee cannot send himself a badge")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class GroupBadges(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    icon = models.ImageField()
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name
