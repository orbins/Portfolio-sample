from .models import Project, Category


def get_categories():
    categories = Category.objects.all()
    return categories
    
    
def get_projects(slug=None):
    if slug:
        items = Project.objects.only('slug', 'image').filter(category__slug=slug).filter(status=True)
        return items
    items = Project.objects.only('slug', 'image').filter(status=True)
    return items
