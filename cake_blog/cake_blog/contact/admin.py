from django.contrib import admin
from .models import Feedback, ContactLink, About, Social, ImageAbout


class ImageAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "email", "create_at"]
    list_display_links = ("name",)
    list_filter = ('create_at', 'name')
    search_fields = ('name', 'email', "phone")
	# prepopulated_fields = {'slug': ('title',)}


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]
    list_display = ["name"]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
	list_display = ['name', 'link']


admin.site.register(ContactLink)
