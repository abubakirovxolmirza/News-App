from django.test import TestCase
from django.contrib.auth.models import User
from .models import News, Comment
# Create your tests here.


class NewsModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='tester1', email='shokh3332@gmail.com', password='tester12.')
        self.news = News.objects.create(
            user=self.user,
            title='Test Title',
            content='Test Content'
        )
        self.comment = Comment.objects.create(user=self.user, news=self.news, comment='Test Comment')

    def test_title(self):
        obj = News.objects.get(id=self.news.id)

        self.assertEqual(obj.title, 'Test Title')

    def test_content(self):
        obj = News.objects.get(id=self.news.id)

        self.assertEqual(obj.content, 'Test Content')
