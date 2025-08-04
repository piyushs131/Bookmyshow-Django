from django.urls import path
from . import views

urlpatterns = [
    path('submit/<str:content_type>/<int:pk>/', views.submit_review, name='submit_review'),
]

    
     
      
       
       