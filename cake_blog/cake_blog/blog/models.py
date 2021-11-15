from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
	name = models.CharField(max_length=100, verbose_name='Категория')
	slug = models.SlugField(max_length=100, verbose_name='Ссылка на категорию')
	parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Главная категория')

	def __str__(self):
		return self.name

	class MPTTMeta:
		order_insertion_by = ['name']


class Tag(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.name


class Post(models.Model):
	author = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE, verbose_name='Автор')
	title = models.CharField(max_length=200, verbose_name='Название')
	image = models.ImageField(upload_to='articles/', verbose_name='Картинка')
	text = RichTextField(verbose_name='Текст поста')
	category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
	tags = models.ManyToManyField(Tag, related_name='post', verbose_name='Хештег')
	create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	slug = models.SlugField(max_length=200, default='', unique=True, verbose_name='Адрес ссылки')
	####################################################
	# status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

	def get_recipes(self):
		return self.recipes.all()

	def get_comments(self):
		return self.comment.all()


class Recipe(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название рецепта')
	serves = models.CharField(max_length=50, verbose_name='Персоны')
	cook_time = models.PositiveIntegerField(default=0, verbose_name='Время приготовления')
	prep_time = models.PositiveIntegerField(default=0, verbose_name='Время подготовки')
	ingredients = RichTextField(verbose_name='Ингредиенты')
	directions = RichTextField(verbose_name='Способ приготовления')
	post = models.ForeignKey(Post, related_name='recipes', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пост')


class Comment(models.Model):
	name = models.CharField(max_length=50, verbose_name="Имя")
	email = models.CharField(max_length=100)
	website = models.CharField(max_length=150, blank=True, null=True)
	message = models.TextField(max_length=500, verbose_name='Сообщение')
	create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE, verbose_name='Пост')