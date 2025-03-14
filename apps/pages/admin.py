from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

from .models import (
    MarketingDepartment, 
    MarketingDepartmentChapters, 
    CompanyAchievements, 
    CompanyAchievementsItems,
    CompanyChallenges,
    CompanyChallengesItems,
    CompanyServices,
    CompanyServicesItems,
    Tags,
    CompanyPosts,
    CompanyPostsItems,
    SocialMedia,
    CompanyPartners,
    CompanyPartnersItems,
    PartnersReviews,
    PartnersReviewsItems,
    CompanyApplication,
    ApplicationForm,
    StaticPages,
    CompanyTeam,
    CompanyTeamItems,
    CompanyAdvertising,
    CompanyAdvertisingItems,
    CompanyVideoReviews,
    CompanyVideoReviewsItems,
    FAQ,
    CompanyBrending,
    CompanyBrendingItems,
    CompanyFeatures,
    CompanyFeaturesItems,
    VideoProduction,
    VideoProductionItems,
    CRMService,
    CRMServiceItems,
    MarketingSupport,
    MarketingSupportItems,
    ServiceOffering,
    ServiceOfferingItems,
    CompanyPostsItemsTasks,
    CompanyPostsItemsImages,
    CompanyPostsItemsResult,
    CompanyPostsItemsTarget,
    BusinessType,
    PromotionType,
    SiteStatusType,
    ServiceType,
    VideoType,
    TaskType,
    CompanyPostsItemsImagesGallery,
    SocialType,
    SiteType,
    BusinessCards,
    BusinessCardImages,
    PrintingService,
    PrintLogo,
    DesignDevelopment,
    DesignDevelopmentChapters,
    Article,
    ArticlePosts,
)

class MarketingDepartmentChaptersInline(StackedInline, TranslationStackedInline):
    model = MarketingDepartmentChapters
    extra = 0   


@admin.register(MarketingDepartment)
class MarketingDepartmentAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [MarketingDepartmentChaptersInline]

    def has_add_permission(self, request):
        return not MarketingDepartment.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class CompanyAchievementsItemsInline(StackedInline, TranslationStackedInline):
    model = CompanyAchievementsItems
    extra = 0


@admin.register(CompanyAchievements)
class CompanyAchievementsAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyAchievementsItemsInline]
    
    def has_add_permission(self, request):
        return not CompanyAchievements.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class CompanyChallengesItemsInline(StackedInline, TranslationStackedInline):
    model = CompanyChallengesItems
    extra = 0


@admin.register(CompanyChallenges)
class CompanyChallengesAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyChallengesItemsInline]
    
    def has_add_permission(self, request):
        return not CompanyChallenges.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class CompanyServicesItemsInline(StackedInline, TranslationStackedInline):
    model = CompanyServicesItems
    extra = 0
    filter_horizontal = ['tags']


@admin.register(CompanyServices)
class CompanyServicesAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyServicesItemsInline]

    def has_add_permission(self, request):
        return not CompanyServices.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Tags)
class TagsAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass


@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass


class CompanyPostsItemsResultInline(StackedInline, TranslationStackedInline):
    model = CompanyPostsItemsResult
    extra = 0
    verbose_name = 'Результат'
    verbose_name_plural = 'Результаты'


class CompanyPostsItemsImagesGalleryInline(SortableInlineAdminMixin, TabularInline):
    model = CompanyPostsItemsImagesGallery
    extra = 1
    fields = ['image']


class CompanyPostsItemsImagesInline(StackedInline, TranslationStackedInline):
    model = CompanyPostsItemsImages
    extra = 0
    verbose_name = 'Изображение'
    verbose_name_plural = 'Изображения'
    show_change_link = True


class CompanyPostsItemsTasksInline(StackedInline, TranslationStackedInline):
    model = CompanyPostsItemsTasks
    extra = 0
    verbose_name = 'Задача'
    verbose_name_plural = 'Задачи'


class CompanyPostsItemsTargetInline(StackedInline, TranslationStackedInline):
    model = CompanyPostsItemsTarget
    extra = 0
    verbose_name = 'Реклама'
    verbose_name_plural = 'Рекламы'


@admin.register(CompanyPostsItemsImages)
class CompanyPostsItemsImagesAdmin(SortableAdminBase, ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyPostsItemsImagesGalleryInline]
    list_display = ['title', 'company_post_item']
    list_filter = ['company_post_item']


@admin.register(CompanyPostsItems)
class CompanyPostsItemsAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyPostsItemsTasksInline, CompanyPostsItemsImagesInline, CompanyPostsItemsResultInline, CompanyPostsItemsTargetInline]
    filter_horizontal = ['tags', 'social_media']


class CompanyPostsItemsInline(StackedInline, TranslationStackedInline):
    model = CompanyPostsItems
    extra = 0
    filter_horizontal = ['tags', 'social_media']
    show_change_link = True


@admin.register(CompanyPosts)
class CompanyPostsAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyPostsItemsInline]

    def has_add_permission(self, request):
        return not CompanyPosts.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class CompanyPartnersItemsInline(StackedInline, TranslationStackedInline):
    model = CompanyPartnersItems
    extra = 0


@admin.register(CompanyPartners)
class CompanyPartnersAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyPartnersItemsInline]

    def has_add_permission(self, request):
        return not CompanyPartners.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class PartnersReviewsItemsInline(StackedInline, TranslationStackedInline):
    model = PartnersReviewsItems
    extra = 0


@admin.register(PartnersReviews)
class PartnersReviewsAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [PartnersReviewsItemsInline]
    
    def has_add_permission(self, request):
        return not PartnersReviews.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CompanyApplication)
class CompanyApplicationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['title']


@admin.register(ApplicationForm)
class ApplicationFormAdmin(ModelAdmin):
    filter_horizontal = ['business_type', 'promotion_type', 'site_status', 'service_type', 'video_type', 'task_type']


@admin.register(StaticPages)
class StaticPagesAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title_ru',)}
    
    class Media:
        js = (
            'admin/js/prepopulate.js',
            'admin/js/prepopulate_init.js',
        )

    def get_prepopulated_fields(self, request, obj=None):
        if obj:
            return {}
        return self.prepopulated_fields


class CompanyTeamItemsInline(StackedInline, TranslationStackedInline):
    model = CompanyTeamItems
    extra = 0


@admin.register(CompanyTeam)
class CompanyTeamAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyTeamItemsInline]

    def has_add_permission(self, request):
        return not CompanyTeam.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class CompanyAdvertisingItemsInline(StackedInline):
    model = CompanyAdvertisingItems
    extra = 0


@admin.register(CompanyAdvertising)
class CompanyAdvertisingAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyAdvertisingItemsInline]

    def has_add_permission(self, request):
        return not CompanyAdvertising.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class CompanyVideoReviewsItemsInline(StackedInline):
    model = CompanyVideoReviewsItems
    extra = 0


@admin.register(CompanyVideoReviews)
class CompanyVideoReviewsAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyVideoReviewsItemsInline]
    list_display = ('title', 'video_type')
    list_filter = ('video_type',)

    def has_add_permission(self, request):
        # Проверяем для каждого типа видео
        existing_types = set(CompanyVideoReviews.objects.values_list('video_type', flat=True))
        # Если есть все типы видео, запрещаем создание
        all_types = {'other', 'production', 'blog'}
        return not all_types.issubset(existing_types)
    
    def has_delete_permission(self, request, obj=None):
        return True

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # Если создаем новую запись
            # Получаем уже использованные типы
            used_types = set(CompanyVideoReviews.objects.values_list('video_type', flat=True))
            # Оставляем только неиспользованные типы в выборе
            choices = [
                choice for choice in form.base_fields['video_type'].choices 
                if choice[0] not in used_types and choice[0] != '---------'
            ]
            if choices:
                form.base_fields['video_type'].choices = choices
                form.base_fields['video_type'].initial = choices[0][0]  # Устанавливаем первый доступный тип по умолчанию
                form.base_fields['video_type'].required = True
            else:
                form.base_fields['video_type'].widget.attrs['disabled'] = True
        return form

    def save_model(self, request, obj, form, change):
        if not change:  # Если создаем новую запись
            # Проверяем, не существует ли уже запись с таким типом
            if CompanyVideoReviews.objects.filter(video_type=obj.video_type).exists():
                from django.core.exceptions import ValidationError
                raise ValidationError(f'Видео отзыв с типом "{obj.get_video_type_display()}" уже существует')
        super().save_model(request, obj, form, change)


@admin.register(FAQ)
class FAQAdmin(ModelAdmin, TabbedTranslationAdmin):
    pass


class CompanyBrendingItemsInline(StackedInline):
    model = CompanyBrendingItems
    extra = 0


@admin.register(CompanyBrending)
class CompanyBrendingAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyBrendingItemsInline]

    def has_add_permission(self, request):
        return not CompanyBrending.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
    

class CompanyFeaturesItemsInline(StackedInline, TranslationStackedInline):
    model = CompanyFeaturesItems
    extra = 0
    filter_horizontal = ['tags']


@admin.register(CompanyFeatures)
class CompanyFeaturesAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CompanyFeaturesItemsInline]

    def has_add_permission(self, request):
        return not CompanyFeatures.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class VideoProductionItemsInline(StackedInline, TranslationStackedInline):
    model = VideoProductionItems
    extra = 0


@admin.register(VideoProduction)
class VideoProductionAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [VideoProductionItemsInline]

    def has_add_permission(self, request):
        return not VideoProduction.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class CRMServiceItemsInline(StackedInline, TranslationStackedInline):
    model = CRMServiceItems
    extra = 0
    filter_horizontal = ['tags']


@admin.register(CRMService)
class CRMServiceAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [CRMServiceItemsInline]

    def has_add_permission(self, request):
        return not CRMService.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class MarketingSupportItemsInline(StackedInline, TranslationStackedInline):
    model = MarketingSupportItems
    extra = 0


@admin.register(MarketingSupport)
class MarketingSupportAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [MarketingSupportItemsInline]

    def has_add_permission(self, request):
        return not MarketingSupport.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class ServiceOfferingItemsInline(StackedInline, TranslationStackedInline):
    model = ServiceOfferingItems
    extra = 0


@admin.register(ServiceOffering)
class ServiceOfferingAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [ServiceOfferingItemsInline]

    def has_add_permission(self, request):
        return not ServiceOffering.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BusinessType)
class BusinessTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


@admin.register(PromotionType)
class PromotionTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


@admin.register(SiteStatusType)
class SiteStatusTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


@admin.register(SiteType)
class SiteTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


@admin.register(ServiceType)
class ServiceTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


@admin.register(VideoType)
class VideoTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


@admin.register(TaskType)
class TaskTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


@admin.register(SocialType)
class SocialTypeAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ['name']


class BusinessCardImagesInline(TabularInline):
    model = BusinessCardImages
    extra = 1


@admin.register(BusinessCards)
class BusinessCardsAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('title',)
    inlines = [BusinessCardImagesInline]


class PrintLogoInline(StackedInline):
    model = PrintLogo
    extra = 0


@admin.register(PrintingService)
class PrintingServiceAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [PrintLogoInline]
    list_display = ('title',)

    def has_add_permission(self, request):
        return not PrintingService.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class DesignDevelopmentChaptersInline(StackedInline, TranslationStackedInline):
    model = DesignDevelopmentChapters
    extra = 0


@admin.register(DesignDevelopment)
class DesignDevelopmentAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [DesignDevelopmentChaptersInline]
    list_display = ('title',)

    def has_add_permission(self, request):
        return not DesignDevelopment.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


class ArticlePostsInline(StackedInline, TranslationStackedInline):
    model = ArticlePosts
    extra = 0


@admin.register(Article)
class ArticleAdmin(ModelAdmin, TabbedTranslationAdmin):
    inlines = [ArticlePostsInline]
    list_display = ('title',)

    def has_add_permission(self, request):
        return not Article.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False
