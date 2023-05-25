from django import template
from portfolio.models import Category

register = template.Library()


@register.inclusion_tag('portfolio/projects_categories.html') #регистрирую тег, с помощью указания пути инициализирую шаблон для рендеринга
def show_categories(): #имя функции - имя inclusion тега, которое используется в шаблоне,для подключения используется имя файла - load menu
    categories = Category.objects.all()
    return {"categories": categories} #возвращаю данные для рендеринга в шаблон
    