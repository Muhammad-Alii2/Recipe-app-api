"""
Tests for the Django admin modifications
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """
    Tests for Django admin
    """

    def setUp(self):
        """
        Create user and client
        """

        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='superuser@example.com',
            password='superpass'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='userpass',
            name='Normal user'
        )

    def test_users_list(self):
        """
        Test users are listed on page
        """

        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_edit_user_page(self):
        """
        Test edit user page works
        """

        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """
        Test create user page works
        """

        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
