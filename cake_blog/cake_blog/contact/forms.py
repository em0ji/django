from django import forms
from .models import Feedback
# from captcha.fields import CaptchaField


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = '__all__'

class FeedbackForm(forms.ModelForm):
	# captcha = CaptchaField()
	class Meta:
		model = Feedback
		# fields = ('name', 'phone', 'email', 'message')
		exclude = ['create_at']
		widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            # 'phone': forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}),
            'phone': forms.TextInput(attrs={'data-mask':"+7 (000) 000-00-00"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Введите сообщение'})
        }

# class Meta:
#     model = Booking
#     fields = ('date', 'contact_number')

#     widgets = {'contact_number': forms.TextInput(attrs={'data-mask':"000-000-0000"})}


