from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to='news_img', blank=True)
    title = models.CharField(max_length=128)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    viewers = models.IntegerField(default=0)

    class Meta:
        db_table = 'News'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


