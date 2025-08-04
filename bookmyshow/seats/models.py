from django.db import models
from movies.models import Movie

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    row = models.CharField(max_length=5)
    number = models.PositiveIntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.row}{self.number} - {self.movie.title}"
    
                            