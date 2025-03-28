# Generated by Django 5.1.5 on 2025-02-04 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0027_companypostsitemsimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPostsItemsResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например: Результаты', max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(help_text='Например: Результаты', max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(help_text='Например: Результаты', max_length=255, null=True, verbose_name='Название')),
                ('title_uz', models.CharField(help_text='Например: Результаты', max_length=255, null=True, verbose_name='Название')),
                ('description', models.TextField(help_text='Например: Мы помогли увеличить выручку корейского ресторана на 70%', verbose_name='Описание')),
                ('description_ru', models.TextField(help_text='Например: Мы помогли увеличить выручку корейского ресторана на 70%', null=True, verbose_name='Описание')),
                ('description_en', models.TextField(help_text='Например: Мы помогли увеличить выручку корейского ресторана на 70%', null=True, verbose_name='Описание')),
                ('description_uz', models.TextField(help_text='Например: Мы помогли увеличить выручку корейского ресторана на 70%', null=True, verbose_name='Описание')),
                ('company_post_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='pages.companypostsitems', verbose_name='Пост компании')),
            ],
            options={
                'verbose_name': 'Результат поста компании',
                'verbose_name_plural': 'Результаты постов компании',
                'ordering': ['-id'],
            },
        ),
    ]
