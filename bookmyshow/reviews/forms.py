from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
        }
        labels = {
            'rating': 'Rating (1-5)',
            'comment': 'Comment',
        }
        help_texts = {
            'rating': 'Rate the movie or event from 1 to 5 stars.',
            'comment': 'Share your thoughts about the movie or event.',
        }           




                                    