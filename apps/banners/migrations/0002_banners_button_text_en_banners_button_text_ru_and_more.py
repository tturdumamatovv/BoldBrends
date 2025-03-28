# Generated by Django 5.1.5 on 2025-02-02 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banners',
            name='button_text_en',
            field=models.CharField(help_text='Например: "Узнать больше"', max_length=255, null=True, verbose_name='Текст кнопки'),
        ),
        migrations.AddField(
            model_name='banners',
            name='button_text_ru',
            field=models.CharField(help_text='Например: "Узнать больше"', max_length=255, null=True, verbose_name='Текст кнопки'),
        ),
        migrations.AddField(
            model_name='banners',
            name='button_text_uz',
            field=models.CharField(help_text='Например: "Узнать больше"', max_length=255, null=True, verbose_name='Текст кнопки'),
        ),
        migrations.AddField(
            model_name='banners',
            name='sub_title_en',
            field=models.CharField(help_text='Например: "Мы поможем вам найти бренды, которые вам нужны"', max_length=255, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='banners',
            name='sub_title_ru',
            field=models.CharField(help_text='Например: "Мы поможем вам найти бренды, которые вам нужны"', max_length=255, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='banners',
            name='sub_title_uz',
            field=models.CharField(help_text='Например: "Мы поможем вам найти бренды, которые вам нужны"', max_length=255, null=True, verbose_name='Подзаголовок'),
        ),
        migrations.AddField(
            model_name='banners',
            name='title_en',
            field=models.CharField(help_text='Например: "Тратите много времени на поиск брендов?"', max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='banners',
            name='title_ru',
            field=models.CharField(help_text='Например: "Тратите много времени на поиск брендов?"', max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='banners',
            name='title_uz',
            field=models.CharField(help_text='Например: "Тратите много времени на поиск брендов?"', max_length=255, null=True, verbose_name='Название'),
        ),
    ]
