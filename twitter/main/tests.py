from django.test import Client
from .serializers import ProfileDetailSerializer
from .models import *
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
# Create your tests here.


class ProfileTests(APITestCase):

    @classmethod
    def setUpTestData(cls):

        Profile.objects.create(
            user_id='1',
            username='Niki',
            email='test@test.ru',
            password='12345'
        )

    def test_username_meta(self):
        user = Profile.objects.get(user_id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_username(self):
        user = Profile.objects.get(user_id=1)
        self.assertEquals('Niki', user.username)
        self.assertEquals('12345', user.password)

    def test_max_length(self):
        user = Profile.objects.get(user_id=1)
        max_length = user._meta.get_field('bio').max_length
        self.assertEquals(max_length, 256)

    def test_create_account(self):
        c = Client()
        url = 'http://127.0.0.1:8000/api/profile/create/'
        data = {
            'user_id': '2',
            'username': 'DabApps',
            'password': '12345',
            'email': 'example@mail.ru'
        }
        response = c.post(url, data, format='json')
        self.assertEqual(Profile.objects.count(), 2)
        self.assertEqual(Profile.objects.get(user_id=2).username, 'DabApps')

    def test_profile_delete(self):
        c = Client()
        url = 'http://127.0.0.1:8000/api/profile/detail/1/'
        response = c.delete(url, data=None, format="json")
        self.assertEqual(Profile.objects.count(), 0)

    def test_login(self):
        client = APIClient()
        client.login(username='Niki', password='12345')


class PostTests(APITestCase):

    @classmethod
    def setUpTestData(cls):

        Profile.objects.create(
            user_id='1',
            username='Niki',
            email='test@test.ru',
            password='12345'
        )
        Post.objects.create(
            author=Profile.objects.get(user_id=1),
            title='TITLE_Заголовок',
            text='Здесь будет чудовищный текст'
        )

    def test_title(self):
        post = Post.objects.get(author=1)
        self.assertEquals('TITLE_Заголовок', post.title)

    def test_post_postCreate(self):
        c = Client()
        url = 'http://127.0.0.1:8000/api/post/add/'
        data = {
            'author': '1',
            'title': 'TITLE_2',
            'text': 'А здесь будет прекрасный текст'
        }
        response = c.post(url, data, format='json')
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.get(id=2).title, 'TITLE_2')

    # def test_post_patch(self):
    #     c = Client()
    #     url = 'http://127.0.0.1:8000/api/post/detail/1/'
    #     data = {
    #         'title': 'TITLE_',
    #     }
    #     response = c.patch(url, data, format='json')
    #     self.assertEqual(Post.objects.get(id=1).title, 'TITLE_')


class ProfileSerializersTest(APITestCase):

    def test_ProfileSerializer(self):
        user_1 = Profile.objects.create(
            user_id='1',
            username='Niki',
            email='test@test.ru',
            password='12345'
        )
        user_2 = Profile.objects.create(
            user_id='2',
            username='Nikolya',
            email='bluff@example.ru',
            password='12345'
        )
        data = ProfileDetailSerializer([user_1, user_2], many=True).data
        expected_data = [
            {
                'user_id': '1',
                'username': 'Niki',
                'email': 'test@test.ru',
                'password': '12345'
            },
            {
                'user_id': '2',
                'username': 'Nikolya',
                'email': 'bluff@example.ru',
                'password': '12345'
            }
        ]
        self.assertEqual(expected_data, data)