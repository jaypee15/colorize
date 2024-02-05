import unittest
from unittest.mock import MagicMock
from django.test import TestCase
from django.urls import reverse
from colors.models import Generation
from colors.views import (
    generations,
    start_generation,
    check_generation,
    complete_generation,
)


class TestGenerationViews(TestCase):

    def test_generations_view(self):
        # Test generations view
        response = self.client.get(reverse("generations"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "generations.html")

        request = MagicMock()
        response = generations(request)
        self.assertEqual(response.status_code, 200)

    def test_start_generation_view(self):
        # Test start_generation view
        request = MagicMock()
        request.POST = {"image_url": "test_image_url"}
        response = start_generation(request)
        self.assertEqual(response.status_code, 200)

    def test_check_generation_view(self):
        # Test check_generation view
        generation = Generation.objects.create(
            secret_key="test_secret_key", before_url="test_image_url", status="started"
        )
        request = MagicMock()
        response = check_generation(request, generation.id)
        self.assertEqual(response.status_code, 200)

    def test_complete_generation_view(self):
        # Test complete_generation view
        generation = Generation.objects.create(
            secret_key="test_secret_key", before_url="test_image_url", status="started"
        )
        request = MagicMock()
        request.method = "POST"
        request.body = '{"output": "test_output_image_url"}'
        response = complete_generation(request, generation.secret_key)
        self.assertEqual(response.status_code, 200)
