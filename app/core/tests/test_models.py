"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """
    Test models
    """

    def test_create_user_with_email_successful(self):
        """
        Test creating a user with an email is successfull
        """

        email = 'testuser@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test email is normalized for new users
        """

        sample_emails = [
            ['testuser1@EXAMPLE.com', 'testuser1@example.com'],
            ['TestUser2@Example.com', 'TestUser2@example.com'],
            ['TESTUSER3@example.com', 'TESTUSER3@example.com'],
            ['testuser4@example.Com', 'testuser4@example.com']
        ]
        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')

            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email_raises_error(self):
        """
        Test creating a user without email raises ValueError
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """
        Test creating a superuser
        """

        user = get_user_model().objects.create_superuser(
            'superuser@example.com',
            'superpass'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
