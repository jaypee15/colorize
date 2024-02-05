from django.test import TestCase
from colors.models import Generation

class GenerationModelTestCase(TestCase):
    def setUp(self):
        self.generation = Generation(
            secret_key="test_key",
            before_url="http://example.com",
            after_url="http://example.com",
        )

    def test_creation(self):
        # Test the creation of a Generation instance
        self.generation.save()
        self.assertIsNotNone(self.generation.id)

 

    def test_str_method(self):
        # Test the __str__ method
        self.assertEqual(
            str(self.generation), "Generation {} | created".format(self.generation.id)
        )

    def test_update(self):
        # Test updating the Generation instance
        new_url = "http://newexample.com"
        self.generation.after_url = new_url
        self.generation.save()
        updated_generation = Generation.objects.get(pk=self.generation.id)
        self.assertEqual(updated_generation.after_url, new_url)