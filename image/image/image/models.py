from django.db import models



class Good(models.Model):
	description_text = models.CharField(max_length=200)
	price_text = models.CharField(max_length=200)
	image_sale = models.ImageField(blank=True, upload_to='images/')

	def __str__(self):
		return self.description_text

	def __str__(self):
		return self.price_text
