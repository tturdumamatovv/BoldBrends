from django.db import models
from django.utils.translation import gettext_lazy as _

class Banners(models.Model):
    title = models.CharField(verbose_name=_('Название'), max_length=255, help_text=_('Например: "Тратите много времени на поиск брендов?"'))
    sub_title = models.CharField(verbose_name=_('Подзаголовок'), max_length=255, help_text=_('Например: "Мы поможем вам найти бренды, которые вам нужны"'))
    button_text = models.CharField(verbose_name=_('Текст кнопки'), max_length=255, help_text=_('Например: "Узнать больше"'))
    image = models.FileField(verbose_name=_('Изображение'), upload_to='banners/')
    is_active = models.BooleanField(verbose_name=_('Активен'), default=True)
    
    class Meta:
        verbose_name = _('Баннер')
        verbose_name_plural = _('Баннеры')
        ordering = ['-id']

    def __str__(self):
        return self.title
