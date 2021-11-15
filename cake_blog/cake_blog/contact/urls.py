from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.FeedbackView.as_view(), name="contact"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('feedback/', views.CreateFeedback.as_view(), name="feedback"),
]