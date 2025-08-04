from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration = models.DurationField(null=True, blank=True)
    poster = models.ImageField(upload_to='movies/', blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.title
