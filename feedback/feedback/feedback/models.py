from django.db import models


class Feedback(models.Model):
	# Класс модели обратной связи
	name = models.CharField(max_length=50, verbose_name='Имя')
	phone = models.CharField(max_length=12, verbose_name='Телефон')
	email = models.EmailField()
	message = models.TextField(max_length=5000, verbose_name='Сообщение')
	create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

	def __str__(self):
		return f'{self.name} - {self.phone} - {self.email}'

	class Meta:
		verbose_name = 'Обратная связь'
		verbose_name_plural = 'Обратная связь'

