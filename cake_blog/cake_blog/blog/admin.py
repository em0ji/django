from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models


class RecipeInLine(admin.StackedInline):
	model = models.Recipe
	extra = 1

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'category', 'author', 'create_at', 'id']
	inlines = [RecipeInLine]
	save_as = True
	save_on_top = True
	##################################################
	list_filter = ('create_at', 'author', 'category')
	search_fields = ('title', 'text')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'create_at'
	# ordering = ('create_at')

@admin.register(models.Recipe)
class PecipeAdmin(admin.ModelAdmin):
	list_display = ['name', 'prep_time', 'cook_time', 'post']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']
    list_filter = ('create_at', 'name')
    search_fields = ('name', 'email')


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
