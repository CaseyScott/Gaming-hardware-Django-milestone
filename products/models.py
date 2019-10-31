from django.db import models

# CATEGORY_CHOICES = (
#     ('Video Cards', 'Video cards'),
#     ('Hard drives', 'Hard drives'),
#     ('Memory', 'Memory'),
#     ('CPU', 'CPU'),
#     ('Cooling', 'Cooling'),
#     ('Motherboards', 'Motherboards'),
#     ('Power supplies', 'Power supplies')
# )


CATEGORY_CHOICES = (
    ('V', 'Video cards'),
    ('H', 'Hard drives'),
    ('M', 'Memory'),
    ('C', 'CPU'),
    ('CL', 'Cooling'),
    ('MB', 'Motherboards'),
    ('P', 'Power supplies')
)

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)

    def __str__(self):
        return self.name
