import factory
from apps.badges.models import Badge, EmployeeBadge


class BadgeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Badge

    id = 1
    title = 'Badge N1'
    description = 'more recently with desktop publishing software '
    picture = factory.django.ImageField(filename="test_picture.jpg")


class EmployeeBadgeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeBadge

    comment = 'Great job'
    employee_guid = 'ade0abcc-308d-4dfe-9f56-76c6717f2a43'
