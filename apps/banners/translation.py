from modeltranslation.translator import register, TranslationOptions

from .models import (
    Banners
)


@register(Banners)
class BannersTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'button_text')