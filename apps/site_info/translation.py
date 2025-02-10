from modeltranslation.translator import register, TranslationOptions

from .models import (
    CompanyInfo,
    Address,
    Phones,
    Emails,
    )


@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('description', 'whatsapp_text', 'work_time')


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('title', 'address')


@register(Phones)
class PhonesTranslationOptions(TranslationOptions):
    fields = ('title', 'phone')

@register(Emails)
class EmailsTranslationOptions(TranslationOptions):
    fields = ('title', 'email')
