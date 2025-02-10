from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Banners

@admin.register(Banners)
class BannersAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    list_editable = ('is_active',)
