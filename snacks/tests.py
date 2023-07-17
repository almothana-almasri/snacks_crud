from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

class SnackTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random', email='random@random.com', password='random@12345'
        )
        self.snack = Snack.objects.create(
            title='Test Snack', purchaser='Test Purchaser', description='Test Description'
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'Test Snack')

    def test_snack_list_view(self):
        url = reverse('snack_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_list.html')

    def test_snack_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_snack_create_view(self):
        url = reverse('snack_create')
        data = {
            "title": "New Snack",
            "purchaser": "New Purchaser",
            "description": "New Description",
        }

        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertEqual(len(Snack.objects.all()), 2)
        self.assertRedirects(response, reverse('snack_detail', args=[2]))

    def test_snack_update_view(self):
        url = reverse('snack_update', args=[self.snack.pk])
        data = {
            "title": "Updated Snack",
            "purchaser": "Updated Purchaser",
            "description": "Updated Description",
        }

        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertEqual(len(Snack.objects.all()), 1)  # No new snack created
        self.snack.refresh_from_db()
        self.assertEqual(self.snack.title, 'Updated Snack')
        self.assertEqual(self.snack.purchaser, 'Updated Purchaser')
        self.assertEqual(self.snack.description, 'Updated Description')

    def test_snack_delete_view(self):
        url = reverse('snack_delete', args=[self.snack.pk])
        response = self.client.post(path=url, follow=True)

        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertEqual(len(Snack.objects.all()), 0)
