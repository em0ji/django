# from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Good


class HomeView(ListView):
	model = Good
	template_name = 'index.html'
