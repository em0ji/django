from ckeditor.fields import RichTextField
from django.db import models


class Feedback(models.Model):
    """ Класс модели обратной связи"""
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.EmailField()
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = 'форму запроса'
        verbose_name_plural = 'Обратная связь'


class ContactLink(models.Model):
    """ Класс модели контактов """
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контактные данные'
        verbose_name_plural = 'Контактные данные'


class About(models.Model):
    """ Класс модели страницы о нас """
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    mini_text = RichTextField()

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'


class ImageAbout(models.Model):
    """ Класс модели изображений страницы о нас """
    image = models.ImageField(upload_to="about/")
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")
    alt = models.CharField(max_length=100)


class Social(models.Model):
    """ Класс модели соцю сетей страницы о нас """
    icon = models.FileField(upload_to="icons/")
    name = models.CharField(max_length=200)
    link = models.URLField()

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'