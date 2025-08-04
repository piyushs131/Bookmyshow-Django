from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie
from events.models import Event

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=[('movie', 'Movie'), ('event', 'Event')])
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content_type} Review"