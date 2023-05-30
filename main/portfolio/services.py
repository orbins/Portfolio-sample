from .models import Project, Category


def get_categories():
    """
    Получение всех категорий
    """
    categories = Category.objects.all()
    return categories
    
    
def get_projects(slug=None):
    """
    Получение проектов, если передан слаг,
    то проекты конкретной категории
    """
    if slug:
        items = Project.objects.only('slug', 'image').filter(category__slug=slug).filter(status=True)
        return items
    items = Project.objects.only('slug', 'image').filter(status=True)
    return items
