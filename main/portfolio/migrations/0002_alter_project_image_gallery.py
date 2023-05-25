# Generated by Django 4.1.4 on 2022-12-25 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, upload_to='logo/%Y/%m/%d', verbose_name='Картинка'),
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='gallery/%Y/%m/%d', verbose_name='Фото')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='portfolio.project', verbose_name='ID проекта')),
            ],
        ),
    ]
