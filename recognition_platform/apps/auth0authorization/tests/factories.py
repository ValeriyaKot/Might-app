import factory
from django.contrib.auth.models import User
from apps.auth0authorization.models import EmployeeInfo


class EmployeeInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeInfo

    user = factory.SubFactory(
        'apps.auth0authorization.tests.conftest.EmployeeFactory',
        employee_info=None
    )
    name = 'Ivan'
    family_name = 'Ivanov'
    role = 'Employee'
    position = 'Software Engineer'


class GroupManagerInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmployeeInfo

    user = factory.SubFactory(
        'apps.auth0authorization.tests.conftest.GroupManagerFactory',
        employee_info=None
    )
    name = 'Ivan'
    family_name = 'Ivanov'
    role = 'Employee'
    position = 'Group Manager'


class GroupManagerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = '2cfa6437-2d61-4242-882c-d19713d5f5d7'
    employee_info = factory.RelatedFactory(
        GroupManagerInfoFactory,
        factory_related_name='user'
    )


class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = '1d457531-7d46-432b-4444-08d7769c61bb'
    employee_info = factory.RelatedFactory(
        EmployeeInfoFactory,
        factory_related_name='user'
    )
