from django import template
from portfolio.models import Category

register = template.Library()


@register.inclusion_tag('portfolio/projects_categories.html')
# регистрирую тег, путь указывает на шаблон для рендеринга
def show_categories():
    # имя функции - имя inclusion-тега, используется в шаблоне,
    # для подключения используется имя файла - load porttag
    categories = Category.objects.all()
    return {"categories": categories}
    # данные для рендеринга в шаблон
    