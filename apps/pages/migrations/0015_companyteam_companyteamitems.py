# Generated by Django 5.1.5 on 2025-02-02 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_companyachievements_sub_title_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например: Команда, которой можно доверять', max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(help_text='Например: Команда, которой можно доверять', max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(help_text='Например: Команда, которой можно доверять', max_length=255, null=True, verbose_name='Название')),
                ('title_uz', models.CharField(help_text='Например: Команда, которой можно доверять', max_length=255, null=True, verbose_name='Название')),
                ('sub_title', models.CharField(help_text='Например: Мы команда, которая поможет вам...', max_length=255, verbose_name='Подзаголовок')),
                ('sub_title_ru', models.CharField(help_text='Например: Мы команда, которая поможет вам...', max_length=255, null=True, verbose_name='Подзаголовок')),
                ('sub_title_en', models.CharField(help_text='Например: Мы команда, которая поможет вам...', max_length=255, null=True, verbose_name='Подзаголовок')),
                ('sub_title_uz', models.CharField(help_text='Например: Мы команда, которая поможет вам...', max_length=255, null=True, verbose_name='Подзаголовок')),
            ],
            options={
                'verbose_name': 'Команда компании',
                'verbose_name_plural': 'Команды компании',
            },
        ),
        migrations.CreateModel(
            name='CompanyTeamItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: Мамбетова Алия', max_length=255, verbose_name='Имя')),
                ('name_ru', models.CharField(help_text='Например: Мамбетова Алия', max_length=255, null=True, verbose_name='Имя')),
                ('name_en', models.CharField(help_text='Например: Мамбетова Алия', max_length=255, null=True, verbose_name='Имя')),
                ('name_uz', models.CharField(help_text='Например: Мамбетова Алия', max_length=255, null=True, verbose_name='Имя')),
                ('position', models.CharField(help_text='Например: Руководитель отдела мобилогрфии', max_length=255, verbose_name='Должность')),
                ('position_ru', models.CharField(help_text='Например: Руководитель отдела мобилогрфии', max_length=255, null=True, verbose_name='Должность')),
                ('position_en', models.CharField(help_text='Например: Руководитель отдела мобилогрфии', max_length=255, null=True, verbose_name='Должность')),
                ('position_uz', models.CharField(help_text='Например: Руководитель отдела мобилогрфии', max_length=255, null=True, verbose_name='Должность')),
                ('image', models.FileField(upload_to='company_team_images/', verbose_name='Изображение')),
                ('company_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pages.companyteam', verbose_name='Команда компании')),
            ],
            options={
                'verbose_name': 'Участник команды компании',
                'verbose_name_plural': 'Участники команды компании',
                'ordering': ['-id'],
            },
        ),
    ]
