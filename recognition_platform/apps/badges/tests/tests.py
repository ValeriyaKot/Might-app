import pytest
import unittest
import json
from rest_framework import status
from .factories import BadgeFactory, EmployeeBadgeFactory
from apps.badges.models import Badge
from apps.auth0authorization.tests.conftest import get_token
from apps.auth0authorization.tests.factories import EmployeeFactory, \
    GroupManagerFactory


@pytest.mark.django_db(transaction=True)
@pytest.mark.usefixtures("inject_attrs")
class BadgeTestCase(unittest.TestCase):
    url = '/badges/'

    def test_returns_badge_list_when_requested(self):
        user = EmployeeFactory()
        BadgeFactory()
        get_token(self.api_client, user)
        response = self.api_client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_creates_badge_by_employee(self):
        user = EmployeeFactory()
        badge = BadgeFactory.build()
        get_token(self.api_client, user)
        badge_data = {
            'title': badge.title,
            'description': badge.description,
            'picture': badge.picture
        }
        response = self.api_client.post(self.url,
                                        data=badge_data,
                                        format='multipart')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_creates_badge_by_group_manager(self):
        user = GroupManagerFactory()
        badge = BadgeFactory.build()
        get_token(self.api_client, user)
        badge_data = {
            'title': badge.title,
            'description': badge.description,
            'picture': badge.picture
        }
        response = self.api_client.post(self.url,
                                        data=badge_data,
                                        format='multipart')
        assert response.status_code == status.HTTP_201_CREATED

    def test_returns_badge_by_id(self):
        user = EmployeeFactory()
        badge = BadgeFactory()
        get_token(self.api_client, user)
        response = self.api_client.get(f'{self.url}{badge.id}/')
        assert response.status_code == status.HTTP_200_OK

    def test_updates_badge_by_employee(self):
        user = EmployeeFactory()
        badge = BadgeFactory()
        badge_data = {
            'title': 'Badge N2',
            'description': 'Badge description',
            'picture': badge.picture
        }
        get_token(self.api_client, user)
        response = self.api_client.put(f'{self.url}{badge.pk}/',
                                       data=badge_data,
                                       format='multipart')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_updates_badge_by_group_manager(self):
        user = GroupManagerFactory()
        badge = BadgeFactory()
        badge_data = {
            'title': 'Badge N2',
            'description': 'Badge description',
            'picture': badge.picture
        }
        get_token(self.api_client, user)
        response = self.api_client.put(
            f'{self.url}{badge.pk}/',
            data=badge_data,
            format='multipart'
        )
        assert response.status_code == status.HTTP_200_OK
        assert json.loads(response.content)['title'] == badge_data['title']
        assert json.loads(response.content)['description'] == badge_data[
            'description']

    def test_deletes_badge_by_group_manager(self):
        user = GroupManagerFactory()
        badge = BadgeFactory()
        get_token(self.api_client, user)
        response = self.api_client.delete(f'{self.url}{badge.pk}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Badge.objects.all().count() == 0


@pytest.mark.django_db(transaction=True)
@pytest.mark.usefixtures("inject_attrs")
class EmployeeBadgeTestCase(unittest.TestCase):
    url = '/employee-badges/'

    def test_returns_badge_list_for_employee(self):
        user = EmployeeFactory()
        badge = BadgeFactory()
        employee_badge = EmployeeBadgeFactory(
            employee_guid=user.username, badge=badge,
            giver_guid='ade0abcc-308d-4dfe-9f56-76c6717f2a43'
        )
        get_token(self.api_client, user)
        response = self.api_client.get(
            f'{self.url}{employee_badge.employee_guid}/'
        )
        assert response.status_code == status.HTTP_200_OK

    def test_assign_badge_for_employee_to_other_employee(self):
        user = EmployeeFactory()
        badge = BadgeFactory()
        get_token(self.api_client, user)
        employee_badge = EmployeeBadgeFactory.build()
        employee_badge_data = {
            'comment': employee_badge.comment,
            'badge': badge.id
        }
        response = self.api_client.post(
            f'{self.url}{employee_badge.employee_guid}/',
            data=employee_badge_data,
            format='multipart'
        )
        print(response.content)
        assert response.status_code == status.HTTP_201_CREATED

    def test_assign_badge_for_yourself(self):
        user = GroupManagerFactory()
        badge = BadgeFactory()
        get_token(self.api_client, user)
        employee_badge = EmployeeBadgeFactory.build()
        employee_badge_data = {
            'badge': badge.id,
            'comment': employee_badge.comment
        }
        response = self.api_client.post(
            f'{self.url}{user.username}/',
            data=employee_badge_data,
            format='multipart'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
