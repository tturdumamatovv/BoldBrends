from django.db import models
from django.utils.translation import gettext_lazy as _


class CompanyInfo(models.Model):
    logo = models.FileField(upload_to='company/logo/', verbose_name=_('Логотип'))
    description = models.TextField(verbose_name=_('Описание'), help_text=_('Например: Bold Brands International ваш внешний отдел маркетинга'))
    whatsapp_logo = models.FileField(upload_to='company/whatsapp_logo/', verbose_name=_('Логотип Whatsapp'))
    whatsapp_link = models.URLField(verbose_name=_('Whatsapp ссылка'), help_text=_('Например: https://wa.me/996555555555'))
    whatsapp_text = models.CharField(verbose_name=_('Текст Whatsapp'), help_text=_('Например: Напишите нам на Whatsapp'), max_length=255)
    work_time = models.CharField(verbose_name=_('Время работы'), help_text=_('Например: Пн-Пт: 09:00-18:00'), max_length=255)
    video = models.FileField(upload_to='company/video/', verbose_name=_('Видео'), help_text=_('Например: https://www.youtube.com/watch?v=dQw4w9WgXcQ'))

    class Meta:
        verbose_name = _('Информация о компании')
        verbose_name_plural = _('Информация о компании')

    def __str__(self):
        return str(_('Информация о компании'))


class Address(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='addresses', verbose_name=_('Компания'))
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Адрес (Бишкек)'))
    address = models.CharField(verbose_name=_('Адрес'), max_length=255, help_text=_('Например: г. Бишкек, ул. Ахунбаева 123'))
    
    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')

    def __str__(self):
        return f"{self.title}: {self.address}"


class Phones(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='phones', verbose_name=_('Компания'))
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Телефон (Бишкек)'))
    phone = models.CharField(verbose_name=_('Телефон'), max_length=255, help_text=_('Например: +996 555 555 555'))

    class Meta:
        verbose_name = _('Телефон')
        verbose_name_plural = _('Телефоны')

    def __str__(self):
        return f"{self.title}: {self.phone}"


class Emails(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='emails', verbose_name=_('Компания'))
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: Email (Бишкек)'))
    email = models.EmailField(verbose_name=_('Email'), max_length=255, help_text=_('Например: info@boldbrands.kg'))

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    def __str__(self):
        return f"{self.title}: {self.email}"


class SocialNetworks(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='social_networks', verbose_name=_('Компания'))
    logo = models.FileField(upload_to='company/social_networks/', verbose_name=_('Логотип'))
    link = models.URLField(verbose_name=_('Ссылка'), help_text=_('Например: https://www.instagram.com/boldbrands.kg'))

    class Meta:
        verbose_name = _('Социальная сеть')
        verbose_name_plural = _('Социальные сети')

    def __str__(self):
        return f"{self.logo}: {self.link}"
