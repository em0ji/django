from django.urls import path
from . import views


urlpatterns = [
    # path('', views.Home)
    path('', views.HomeView.as_view(), name='home'),
]