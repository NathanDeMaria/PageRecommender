from django.db import models


class Article(models.Model):
    RESPONSES = (
        ('L', 'like'),
        ('D', 'dislike')
    )
    url = models.CharField(max_length=100)
    access_time = models.DateField()
    response = models.CharField(max_length=1, choices=RESPONSES)
