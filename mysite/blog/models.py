from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # pub_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title