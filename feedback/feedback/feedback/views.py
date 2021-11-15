from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect

from .forms import FeedbackForm
from .models import Feedback


class Base(ListView):
	model = Feedback
	template_name = 'base.html'
# 	success_url = "/"

# def Home(request):
# 	return render(request, 'base.html')


class FeedbackDetailView(DetailView):
	model = Feedback


	# def get(self, request):
	# 	contacts = ContactLink.objects.all()
	# 	form = FeedbackForm()
	# 	phone = 'phone'
	# 	if 'tel' in request.POST:
	# 		phone = request.POST['tel']
	# 	return render(request, 'base.html', {"form": form})


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = FeedbackForm()
		return context


# class CreateFeedback(CreateView):
# 	form_class = FeedbackForm
# 	success_url = '/'
