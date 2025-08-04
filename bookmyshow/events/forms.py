from django import forms
from .models import Event, EventCategory

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['category', 'title', 'date', 'venue', 'price', 'description']

class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ['name']
