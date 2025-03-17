# analytics/models.py
from django.db import models

class PostAnalytics(models.Model):
    post_id = models.IntegerField(null=True, blank=True)  
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Post {self.post_id} viewed at {self.timestamp}"
