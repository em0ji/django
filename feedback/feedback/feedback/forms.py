from django import forms
from .models import Feedback
from captcha.fields import CaptchaField


class FeedbackForm(forms.ModelForm):
	captcha = CaptchaField()
	class Meta:
		model = Feedback
		fields = ['name', 'phone', 'email', 'message']
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
			'phone': forms.TextInput(attrs={'placeholder': 'Введите номер'}),
			'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
			'message': forms.Textarea(attrs={'placeholder': 'Введите сообщение'})
		}
