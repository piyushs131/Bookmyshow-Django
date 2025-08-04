from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['movie', 'event']
        widgets = {
            'movie': forms.Select(attrs={'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'movie': 'Select Movie',
            'event': 'Select Event',
        }   
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['movie'].queryset = user.movies.all()
            self.fields['event'].queryset = user.events.all()
        else:
            self.fields['movie'].queryset = Booking.objects.none()
            self.fields['event'].queryset = Booking.objects.none()      
    def clean(self):
        cleaned_data = super().clean()
        movie = cleaned_data.get('movie')
        event = cleaned_data.get('event')

        if not movie and not event:
            raise forms.ValidationError("You must select either a movie or an event.")

        return cleaned_data     
    def save(self, commit=True):
        booking = super().save(commit=False)
        if commit:
            booking.save()
        return booking  
    def get_user_bookings(self, user):
        """
        Returns a queryset of bookings for the given user.
        """
        return Booking.objects.filter(user=user)            
