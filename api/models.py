from django.db import models


class ContentUpload(models.Model):
    # You can store the active section type if needed
    SECTION_CHOICES = [
        ('home', 'Home'),
        ('news', 'News'),
        ('tv', 'TV'),
        ('events', 'Events'),
    ]
    file = models.FileField(upload_to='uploads/')
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    region = models.CharField(max_length=100, blank=True)
    youtube_url = models.URLField(blank=True)
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or 'Content Upload'


class MagazineContent(models.Model):
    cover_image = models.ImageField(upload_to='magazines/')
    title = models.CharField(max_length=255)
    date = models.DateField()
    summary = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title