from django import template
from portfolio.models import Category

register = template.Library()


@register.inclusion_tag('portfolio/projects_categories.html')
def show_categories():
    """
    Тег для отображения категорий
    """
    categories = Category.objects.all()
    return {"categories": categories}
    