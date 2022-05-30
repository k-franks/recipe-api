"""
Test for models
"""
from decimal import Decimal

from core import models
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_succesful(self):
        """Test creating user with an email succesfull"""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test new user without email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """Test create superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe"""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'pass1234',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample Recipe Name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Recipe Description'
        )

        self.assertEqual(str(recipe), recipe.title)
