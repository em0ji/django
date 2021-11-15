from django.urls import path
from . import views


urlpatterns = [
    
    # path('feedback/', views.FeedbackView.as_view(), name="feedback"),
    # path('', views.CreateFeedback.as_view(), name="create"),
    path('', views.Base.as_view(), name="home"),
    # path('', views.Home, name="home"),
]