from django.contrib import admin
from .models import Project, Category, Tag, Gallery
from django.utils.safestring import mark_safe


class GalleryAdmin(admin.StackedInline):
    model = Gallery
    fields = ('photo', 'project')
    save_as = True
    save_on_top = True


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'created_at', 'category', 'get_image', 'status',)
    list_display_links = ('slug', 'title')
    save_as = True
    save_on_top = True
    search_fields = ('title',)
    search_help_text = 'Введите название проекта'
    list_filter = ('category', 'tags',)
    readonly_fields = ('views', 'created_at', 'get_image') #2
    fields = ('title', 'slug', 'category', 'tags', 'content', 'image', 'get_image', 'created_at', 'status', 'views')
    # Отображение в форме для отдельно взятого проекта, порядок учитывается
    inlines = [GalleryAdmin]
    # класс встроенной модели указываю здесь
    
    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src = "{obj.image.url}" width = "50px" height = "50px">')
        return '-'
  
    get_image.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# inline класс не регистрируется
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
