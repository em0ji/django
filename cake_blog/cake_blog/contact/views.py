from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .models import ContactLink, About, Feedback
from .forms import FeedbackForm



class FeedbackView(View):
	def get(self, request):
		contacts = ContactLink.objects.all()
		form = FeedbackForm()
		# phone = 'phone'
		# if 'tel' in request.POST:
		# 	phone = request.POST['tel']
		return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})


class CreateFeedback(CreateView):
	form_class = FeedbackForm
	# template_name = 'blog/home.html'
	success_url = '/'

				

class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {"about": about})