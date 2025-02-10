from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline, TranslationStackedInline
from .models import CompanyInfo, Address, Phones, Emails, SocialNetworks

class AddressInline(StackedInline, TranslationStackedInline):
    model = Address
    extra = 0


class PhonesInline(StackedInline, TranslationStackedInline):
    model = Phones
    extra = 0


class EmailsInline(StackedInline, TranslationStackedInline):
    model = Emails
    extra = 0


class SocialNetworksInline(TabularInline):
    model = SocialNetworks
    extra = 0


@admin.register(CompanyInfo)
class CompanyInfoAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [AddressInline, PhonesInline, EmailsInline, SocialNetworksInline]
    
    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
