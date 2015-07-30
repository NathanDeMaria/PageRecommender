from django.db import models


class Article(models.Model):
    RESPONSES = (
        ('L', 'like'),
        ('D', 'dislike')
    )
    url = models.CharField(max_length=256)
    body_text = models.TextField()
    access_time = models.DateTimeField()
    response = models.CharField(max_length=1, choices=RESPONSES)
