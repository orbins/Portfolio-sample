# Generated by Django 4.1.4 on 2022-12-19 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория(ю)',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'db_table': 'tags',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.FileField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Картинка')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.BooleanField(default=True, verbose_name='Статус')),
                ('views', models.IntegerField(default=0, verbose_name='К-во просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(blank=True, related_name='projects', to='portfolio.tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'db_table': 'projects',
                'ordering': ['-created_at'],
            },
        ),
    ]
