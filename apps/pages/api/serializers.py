from rest_framework import serializers

from apps.pages.models import (
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
    BusinessType,
    PromotionType,
)

class MarketingDepartmentChaptersSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingDepartmentChapters
        fields = ('number', 'title')


class MarketingDepartmentSerializer(serializers.ModelSerializer):
    chapters = MarketingDepartmentChaptersSerializer(many=True, read_only=True)

    class Meta:
        model = MarketingDepartment
        fields = ('title', 'sub_title', 'chapters')


class CompanyAchievementsItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAchievementsItems
        fields = ('title', 'sub_title')


class CompanyAchievementsSerializer(serializers.ModelSerializer):
    items = CompanyAchievementsItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyAchievements
        fields = ('title', 'sub_title', 'items')


class CompanyChallengesItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyChallengesItems
        fields = ('logo', 'title', 'description')


class CompanyChallengesSerializers(serializers.ModelSerializer):
    items = CompanyChallengesItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyChallenges
        fields = ('title', 'items')


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('tags',)


class CompanyServicesItemsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyServicesItems
        fields = ('title', 'image', 'tags')


class CompanyServicesSerializer(serializers.ModelSerializer):
    items = CompanyServicesItemsSerializer(many=True, read_only=True)
    class Meta:
        model = CompanyServices
        fields = ('title', 'items')


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('title', 'logo', 'subscribers')


class CompanyPostsItemsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    social_media = SocialMediaSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyPostsItems
        fields = ('image', 'title', 'company_name', 'created_at', 'tags', 'social_media')


class CompanyPostsSerializer(serializers.ModelSerializer):
    items = CompanyPostsItemsSerializer(source='items_limited', many=True, read_only=True)

    class Meta:
        model = CompanyPosts
        fields = ('title', 'items')


class CompanyPartnersItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPartnersItems
        fields = ('company_name', 'company_logo')


class CompanyPartnersSerializer(serializers.ModelSerializer):
    items = CompanyPartnersItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyPartners
        fields = ('title', 'items')


class PartnersReviewsItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersReviewsItems
        fields = ('rating', 'user_image', 'user_name', 'user_position', 'text')


class PartnersReviewsSerializer(serializers.ModelSerializer):
    items = PartnersReviewsItemsSerializer(many=True, read_only=True)

    class Meta:
        model = PartnersReviews
        fields = ('title', 'description', 'items')


class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = ('id', 'name')


class PromotionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionType
        fields = ('id', 'name')


class ApplicationFormSerializer(serializers.ModelSerializer):
    business_type = serializers.PrimaryKeyRelatedField(many=True, queryset=BusinessType.objects.all())
    promotion_type = serializers.PrimaryKeyRelatedField(many=True, queryset=PromotionType.objects.all())

    class Meta:
        model = ApplicationForm
        fields = ('sender_name', 'sender_phone', 'sender_email', 'business_type', 'promotion_type')


class CompanyApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyApplication
        fields = ('title', 'sub_title')


class StaticPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticPages
        fields = ('title', 'content', 'image', 'slug')


class CompanyTeamItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTeamItems
        fields = ('name', 'position', 'image')


class CompanyTeamSerializer(serializers.ModelSerializer):
    items = CompanyTeamItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyTeam
        fields = ('title', 'sub_title', 'items')


class CompanyAdvertisingItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAdvertisingItems
        fields = ('image',)


class CompanyAdvertisingSerializer(serializers.ModelSerializer):
    items = CompanyAdvertisingItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyAdvertising
        fields = ('title', 'sub_title', 'items')


class CompanyVideoReviewsItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyVideoReviewsItems
        fields = ('video',)


class CompanyVideoReviewsSerializer(serializers.ModelSerializer):
    items = CompanyVideoReviewsItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyVideoReviews
        fields = ('title', 'sub_title', 'items')


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('question', 'answer')


class CompanyBrendingItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBrendingItems
        fields = ('image',)



class CompanyBrendingSerializer(serializers.ModelSerializer):
    items = CompanyBrendingItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyBrending
        fields = ('title', 'sub_title', 'sub_title_2', 'items')


class CompanyFeaturesItemsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyFeaturesItems
        fields = ('image', 'image_right', 'title', 'sub_title', 'description', 'tags')



class CompanyFeaturesSerializer(serializers.ModelSerializer):
    items = CompanyFeaturesItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyFeatures
        fields = ('title', 'items')


class VideoProductionItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoProductionItems
        fields = ('video', 'logo', 'title', 'description')


class VideoProductionSerializer(serializers.ModelSerializer):
    items = VideoProductionItemsSerializer(many=True, read_only=True)

    class Meta:
        model = VideoProduction
        fields = ('title', 'description', 'items')


class CRMServiceItemsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)

    class Meta:
        model = CRMServiceItems
        fields = ('image', 'image_right', 'title', 'tags')


class CRMServiceSerializer(serializers.ModelSerializer):
    items = CRMServiceItemsSerializer(many=True, read_only=True)

    class Meta:
        model = CRMService
        fields = ('title', 'items')



class MarketingSupportItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingSupportItems
        fields = ('logo', 'title', 'description', 'video')


class MarketingSupportSerializer(serializers.ModelSerializer):
    items = MarketingSupportItemsSerializer(many=True, read_only=True)

    class Meta:
        model = MarketingSupport
        fields = ('title', 'description', 'items')


class ServiceOfferingItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceOfferingItems
        fields = ('image', 'image_right', 'title', 'description')


class ServiceOfferingSerializer(serializers.ModelSerializer):
    items = ServiceOfferingItemsSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceOffering
        fields = ('title', 'items')


class CompanyPostsItemsTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPostsItemsTasks
        fields = ('title', 'description')


class CompanyPostsItemsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPostsItemsImages
        fields = ('title', 'image', 'description')


class CompanyPostsItemsResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPostsItemsResult
        fields = ('header', 'title', 'description')


class CompanyPostsItemsDetailSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    social_media = SocialMediaSerializer(many=True, read_only=True)
    tasks = CompanyPostsItemsTasksSerializer(many=True, read_only=True)
    images = CompanyPostsItemsImagesSerializer(many=True, read_only=True)
    results = CompanyPostsItemsResultSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyPostsItems
        fields = (
            'id',
            'image',
            'title',
            'company_name',
            'created_at',
            'tags',
            'social_media',
            'tasks',
            'images',
            'results'
        )
