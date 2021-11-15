from django import forms
from .models import Feedback
# from captcha.fields import CaptchaField


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = '__all__'


class FeedbackForm(forms.ModelForm):
# 	captcha = CaptchaField()
	class Meta:
		model = Feedback
		fields = '__all__'
	# 	exclude = ['create_at']
	# 	widgets = {
	# 	'phone': forms.TextInput(attrs={'placeholder': 'phone'}),
 #            	'name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
 #            	'email': forms.EmailInput(attrs={'placeholder': 'Введите email'}),
 #            	'message': forms.Textarea(attrs={'placeholder': 'Введите сообщение'})
 #        }


#Форма из блога коммент
# class CommentForm(forms.ModelForm):
# 	captcha = CaptchaField()
# 	class Meta:
# 		model = Comment
# 		exclude = ['create_at', 'post']
# 		widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'name'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'email'}),
#             'website': forms.TextInput(attrs={'placeholder': 'website'}),
#             'message': forms.Textarea(attrs={'placeholder': 'message'})
#         }