from django.db import models
from django.conf import settings
from movies.models import Movie
from events.models import Event

class Booking(models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.SET_NULL)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    booked_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username} for {'Movie: ' + str(self.movie) if self.movie else 'Event: ' + str(self.event)}"
    