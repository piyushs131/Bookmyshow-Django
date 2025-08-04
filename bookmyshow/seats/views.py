from django.shortcuts import render, get_object_or_404, redirect
from .models import Seat
from movies.models import Movie


def select_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seats')
        for seat_id in selected_seats:
            seat = Seat.objects.get(id=seat_id)
            seat.is_booked = True
            seat.save()
        return redirect('booking_history')

    return render(request, 'seats/select_seat.html', {'movie': movie, 'seats': seats})

     
      
       
          