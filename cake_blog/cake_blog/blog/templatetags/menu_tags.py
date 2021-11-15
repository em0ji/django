from django import template
from blog.models import Category, Post

register = template.Library()


# Начало тегов отвечающих за вложенность категорий sidebar (get_list_category) и top_menu (get_categories)
def get_all_categories():
    return Category.objects.all()

@register.simple_tag()
def get_list_category():
    """Вывод всех категорий"""
    return get_all_categories()

@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    category = get_all_categories()
    # category = Category.objects.filter(parent__isnull=True).order_by('name')
    return {"list_category": category}
# Конец тегов отвечающих за вложенность категорий меню и sidebar


@register.inclusion_tag('blog/include/tags/recipes_tag.html')
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:5]
    return {"list_last_post": posts}