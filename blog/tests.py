from django.test import TestCase
from django.urls import reverse
from . models import Post

class UrlsTests(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Добро пожаловать в мой блог!")  # Проверяем наличие текста

    def test_about_url(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        response = self.client.get(reverse('post_detail', args=[1]))  # Тестируем маршрут поста с ID 1
        self.assertEqual(response.status_code, 200)

    def test_invalid_url(self):
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)


class FormTests(TestCase):
    def test_create_post_form(self):
        response = self.client.post(reverse('post_create'), {
            'title': 'New Post',
            'content': 'New content',
        })
        self.assertEqual(response.status_code, 302)  # Проверяем, что происходит перенаправление
        self.assertTrue(Post.objects.filter(title='New Post').exists())  # Проверяем, что пост был создан
