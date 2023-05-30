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
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги", related_name="projects")
    status = models.BooleanField(default=True, verbose_name="Статус")
    views = models.IntegerField(default=0, verbose_name="К-во просмотров")
    
    class Meta:
        ordering = ['-created_at']
        db_table = 'projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        # при добавлении нового объекта или изменении
        super().save(*args, **kwargs)
        if self.image:
            # Если поле изображения объекта не пустое
            with Image.open(self.image) as image:
                image = image.resize((900, 800))
                image.save(self.image.path)

    def get_absolute_url(self):
        return reverse('single', kwargs={'slug': self.slug})


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
