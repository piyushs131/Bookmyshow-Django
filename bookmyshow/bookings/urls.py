from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('remove/<int:booking_id>/', views.remove_booking, name='remove_booking'),
    path('add_movie/<int:movie_id>/', views.add_booking_movie, name='add_booking'),
    path('add_event/<int:event_id>/', views.add_booking_event, name='add_booking_event'),
]