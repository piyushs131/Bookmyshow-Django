from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from events.models import Event
from .models import Booking

@login_required
def add_booking_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    Booking.objects.create(user=request.user, movie=movie)
    return redirect('movie_list')

@login_required
def add_booking_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    Booking.objects.create(user=request.user, event=event)
    return redirect('event_list')

@login_required
def cart_view(request):
    bookings = Booking.objects.filter(user=request.user, paid=False)
    return render(request, 'bookings/cart.html', {'bookings': bookings})

@login_required
def remove_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    booking.delete()
    return redirect('cart')

@login_required
def checkout(request):
    Booking.objects.filter(user=request.user, paid=False).update(paid=True)
    return render(request, 'bookings/checkout_success.html')
