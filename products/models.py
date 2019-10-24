from django.db import models

CATEGORY_CHOICES = (
    ('V', 'video cards'),
    ('H', 'hard drives'),
    ('M', 'memory'),
    ('C', 'cpu'),
    ('CL', 'cooling'),
    ('MB', 'mother boards'),
    ('P', 'power supplies')
)

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return self.name
