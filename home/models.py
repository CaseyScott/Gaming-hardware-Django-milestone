from django.db import models


class BannerPost(models.Model):
    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
