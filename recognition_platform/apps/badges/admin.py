from django.contrib import admin
from .models import Badge, EmployeeBadge, GroupBadges


admin.site.register(Badge)
admin.site.register(EmployeeBadge)
admin.site.register(GroupBadges)
