from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


# Create your models here.

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_search')
    time = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=264)
    result = models.URLField()
    history = HistoricalRecords()

    def __str__(self):
        return self.keyword
