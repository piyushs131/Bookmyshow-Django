from django.urls import path
from . import views

urlpatterns = [
    path('select/<int:movie_id>/', views.select_seat, name='select_seat'),
]