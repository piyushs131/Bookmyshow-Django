from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review
from movies.models import Movie
from events.models import Event

def submit_review(request, content_type, pk):
    if content_type == 'movie':
        item = get_object_or_404(Movie, pk=pk)
    else:
        item = get_object_or_404(Event, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.content_type = content_type
            if content_type == 'movie':
                review.movie = item
            else:
                review.event = item
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_form.html', {'form': form, 'item': item})


    


                      