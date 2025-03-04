from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from .models import Banners, BannerText

class BannerTextInline(TabularInline, TranslationStackedInline):
    model = BannerText
    extra = 1
    max_num = 1  # Ограничиваем максимальное количество записей до 1

@admin.register(Banners)
class BannersAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('is_active',)
    inlines = [BannerTextInline]
