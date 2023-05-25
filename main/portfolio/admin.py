from django.contrib import admin
from .models import Project, Category, Tag, Gallery
from django.utils.safestring import mark_safe


class GalleryAdmin(admin.StackedInline):
    # Класс редактор для настройки представления моделей в админке
    model = Gallery
    # 1) Модель, с которой связан класс, указываю здесь
    fields = ('photo', 'get_image', 'project')
    save_as = True
    save_on_top = True


class ProjectAdmin(admin.ModelAdmin):
    # Класс редактор для настройки представления моделей в админке
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'created_at', 'category', 'get_image', 'status',)
    list_display_links = ('slug', 'title')
    save_as = True #
    # Добавляется кнопка сохранить как новый объект
    save_on_top = True
    search_field = ('title',)
    list_filter = ('category', 'tags',)
    readonly_fields = ('views', 'created_at', 'get_image') 
    fields = ('title', 'slug', 'category', 'tags', 'content', 'image', 'get_image', 'created_at', 'status', 'views')
    # Отображение в форме для отдельно взятого проекта, порядок учитывается
    inlines = [GalleryAdmin]
    # 2) класс встроенной модели указываю здесь в спец. параметре inlines
    
    def get_image(self, obj):
        if obj.image:
            # Если у статьи(экземпляра модели - self) есть атрибут фото (Чем тогда является self - атрибут класса projectadmin)
            return mark_safe(f'<img src = "{obj.image.url}" width = "50px" height = "50px">')
            # Возвращает не url, а саму картинку
        return '-'
        # Если фото нет
  
    get_image.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Gallery)
# 3) Регистрирую просто модель, особенности класса inline, т.к класс inline будет отображаться в другом классе, там я его и указал
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
