from modeltranslation.translator import register, TranslationOptions
from .models import (
    StaticPages,
    MarketingDepartment,
    MarketingDepartmentChapters,
    CompanyAchievements,
    CompanyAchievementsItems,
    CompanyChallenges,
    CompanyChallengesItems,
    CompanyServices,
    Tags,
    SocialMedia,
    CompanyServicesItems,
    CompanyPosts,
    CompanyPostsItems,
    CompanyPartners,
    CompanyPartnersItems,
    PartnersReviews,
    PartnersReviewsItems,
    CompanyApplication,
    CompanyTeam,
    CompanyTeamItems,
    CompanyAdvertising,
    CompanyVideoReviews,
    FAQ,
    CompanyBrending,
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
    CompanyPostsItemsTarget,
    CompanyPostsItemsImages,
    CompanyPostsItemsResult,
    BusinessType,
    PromotionType,
    SiteStatusType,
    SiteType,
    ServiceType,
    VideoType,
    TaskType,
    SocialType,
    BusinessCards,
    PrintingService,
    PrintLogo
)

@register(StaticPages)
class StaticPagesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')  # поля, которые нужно перевести 


@register(MarketingDepartment)
class MarketingDepartmentTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(MarketingDepartmentChapters)
class MarketingDepartmentChaptersTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CompanyAchievements)
class CompanyAchievementsTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(CompanyAchievementsItems)
class CompanyAchievementsItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(CompanyChallenges)
class CompanyChallengesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CompanyChallengesItems)
class CompanyChallengesItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CompanyServices)
class CompanyServicesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Tags)
class TagsTranslationOptions(TranslationOptions):
    fields = ('tags',)


@register(SocialMedia)
class SocialMediaTranslationOptions(TranslationOptions):
    fields = ('title', 'subscribers')


@register(CompanyServicesItems)
class CompanyServicesItemsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CompanyPosts)
class CompanyPostsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CompanyPostsItems)
class CompanyPostsItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'company_name')


@register(CompanyPartners)
class CompanyPartnersTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CompanyPartnersItems)
class CompanyPartnersItemsTranslationOptions(TranslationOptions):
    fields = ('company_name',)



@register(PartnersReviews)
class PartnersReviewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(PartnersReviewsItems)
class PartnersReviewsItemsTranslationOptions(TranslationOptions):
    fields = ('user_name', 'user_position', 'text')


@register(CompanyApplication)
class CompanyApplicationTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(CompanyTeam)
class CompanyTeamTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(CompanyTeamItems)
class CompanyTeamItemsTranslationOptions(TranslationOptions):
    fields = ('name', 'position')


@register(CompanyAdvertising)
class CompanyAdvertisingTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(CompanyVideoReviews)
class CompanyVideoReviewsTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(CompanyBrending)
class CompanyBrendingTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'sub_title_2')


@register(CompanyFeatures)
class CompanyFeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CompanyFeaturesItems)
class CompanyFeaturesItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'description')


@register(VideoProduction)
class VideoProductionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(VideoProductionItems)
class VideoProductionItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CRMService)
class CRMServiceTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CRMServiceItems)
class CRMServiceItemsTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(MarketingSupport)
class MarketingSupportTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(MarketingSupportItems)
class MarketingSupportItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ServiceOffering)
class ServiceOfferingTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ServiceOfferingItems)
class ServiceOfferingItemsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CompanyPostsItemsTasks)
class CompanyPostsItemsTasksTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CompanyPostsItemsTarget)
class CompanyPostsItemsTargetTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CompanyPostsItemsImages)
class CompanyPostsItemsImagesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CompanyPostsItemsResult)
class CompanyPostsItemsResultTranslationOptions(TranslationOptions):
    fields = ('header', 'title', 'description')


@register(BusinessType)
class BusinessTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(PromotionType)
class PromotionTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(SiteStatusType)
class SiteStatusTypeTranslationOption(TranslationOptions):
    fields = ('name',)


@register(SiteType)
class SiteTypeTranslationOption(TranslationOptions):
    fields = ('name',)


@register(ServiceType)
class ServiceTypeTranslationOption(TranslationOptions):
    fields = ('name',)


@register(VideoType)
class VideoTypeTranslationOption(TranslationOptions):
    fields = ('name',)


@register(TaskType)
class TaskTypeTranslationOption(TranslationOptions):
    fields = ('name',)


@register(SocialType)
class SocialTypeTranslationOption(TranslationOptions):
    fields = ('name',)


@register(BusinessCards)
class BusinessCardsTranslationOption(TranslationOptions):
    fields = ('title',)


@register(PrintingService)
class PrintingServiceTranslationOptions(TranslationOptions):
    fields = ('title',)
    