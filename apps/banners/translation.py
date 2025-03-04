from modeltranslation.translator import register, TranslationOptions

from .models import (
    Banners,
    BannerText
)


@register(Banners)
class BannersTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'button_text')

@register(BannerText)
class BannerTextTranslationOptions(TranslationOptions):
    fields = ('text',)