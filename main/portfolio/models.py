from django.db import models
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})
        # 1 параметр - название маршрута, 2 параметр - динамический для ссылок, category_id (ключ) имя из urls, параметр маршрутизатора, значение ему присваивалось в шаблоне и ему соответствует id экземпляра модели
        # в шаблоне я обращаюсь к методу экземпляра модели и  он создаст путь по наименованию маршрута из маршрутизатора (точно такой же), а динамическому парамтеру маршрута (который совпадает здесь с тем, что указан в маршрутизаторе) присвоит значение атрибута объекта модели 
    
    class Meta:
        ordering = ['title']  
        db_table = 'categories'
        verbose_name = "Категория(ю)"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name="URL", unique=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title'] 
        db_table = 'tags'
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, verbose_name="URL", unique=True)
    content = models.TextField(verbose_name="Описание", blank=True)
    image = models.FileField(upload_to=f"logo/%Y/%m/%d", verbose_name="Картинка", blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="projects")
    # related_name используется вместо set. Т.е у класса Category появится свойство posts (У post есть свойство category) Type of work (pet-project, freelance, team work)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги", related_name="projects")
    # Создаст связующую таблицу, между постами и тегами, в которую будет записываться id поста и id тега для этого поста
    status = models.BooleanField(default=True, verbose_name="Статус")
    views = models.IntegerField(default=0, verbose_name="К-во просмотров")
    # Project - вторичная модель, у 1 катгории множество проектов, у множества тегов множество проектов
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        # Модель регистрируется в админке и при добавлении её нового объекта или её изменении, запускается метод save
        # Вызывается метод save класса (модели) и просто дополняется следующими строчками #Аргументы в super - необязательны, класс который наследуем и объект, к которому привязываем метод save
        super().save(*args, **kwargs)
        if self.image:
            # Если поле изображения объекта не пустое
            with Image.open(self.image) as image:
                # С помощью метода open класса Image (модуля Pillow) открывается файл с изображением
                image = image.resize((900, 800))
                # Меняется его размер, resize возвращает новый объект
                image.save(self.image.path) #
                # Новое фото сохраняется в объект
    
    
    def get_absolute_url(self):
        # self означает экземпляр, который передаётся в метод/к которому принадлежит метод
        return reverse('single', kwargs={'slug': self.slug})
        # 1 параметр - название маршрута, 2 параметр - динамический для ссылок, category_id (ключ) имя из urls, параметр маршрутизатора, значение ему присваивалось в шаблоне и ему соответствует id экземпляра модели
        # в шаблоне я обращаюсь к методу экземпляра модели и  он создаст путь по наименованию маршрута из маршрутизатора (точно такой же), а динамическому парамтеру маршрута (который совпадает здесь с тем, что указан в маршрутизаторе) присвоит значение атрибута объекта модели 


class Gallery(models.Model):
    photo = models.ImageField(upload_to="gallery/%Y/%m/%d", verbose_name="Фото", blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект", related_name="photos")
    
    class Meta:
        verbose_name = "Картинка для галереи"
        verbose_name_plural = "Картинки для галереи"
    
    def __str__(self):
        return f"Картинка №{self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            with Image.open(self.photo) as image:
                image = image.resize((900, 800))
                image.save(self.photo.path)
