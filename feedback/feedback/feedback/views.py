from django.views.generic import CreateView
from .forms import FeedbackForm
from .models import Feedback
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.mail import send_mail


class FeedbackCreate(CreateView):
	model = Feedback
	# fields = ["first_name", "last_name", "message"]
	success_url = reverse_lazy('success_page')
	form_class = FeedbackForm


	def form_valid(self, form):
	# Формируем сообщение для отправки
		data = form.data
		subject = f'Сообщение с формы от {data["name"]} {data["phone"]} Почта отправителя: {data["email"]}'
		# email(subject, data['message'])
		return super().form_valid(form)


# Функция отправки сообщения
# def email(subject, content):
#    send_mail(subject,
#       content,
#       'отправитель@gmail.com',
#       ['получатель1@gmail.com']
#    )


# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   return HttpResponse('Письмо отправлено! Ожидайте, с вами свяжутся!')
