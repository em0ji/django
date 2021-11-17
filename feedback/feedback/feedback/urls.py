from django.urls import path
from feedback.views import FeedbackCreate, success



urlpatterns = [
    
    path('', FeedbackCreate.as_view(), name='feedback'),
    path('success/', success, name='success_page')

]