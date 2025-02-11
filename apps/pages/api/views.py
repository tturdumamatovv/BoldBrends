from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.pagination import PageNumberPagination

from apps.pages.models import (
    MarketingDepartment, 
    CompanyAchievements, 
    CompanyChallenges,
    CompanyServices,
    CompanyPosts,
    CompanyPartners,
    PartnersReviews,
    CompanyApplication,
    StaticPages,
    CompanyTeam,
    CompanyAdvertising,
    CompanyVideoReviews,
    FAQ,
    CompanyBrending,
    CompanyFeatures,
    VideoProduction,
    CRMService,
    MarketingSupport,
    ServiceOffering,
    CompanyPostsItems,
    Tags,
    BusinessType,
    PromotionType,
    )

from .serializers import (  
    MarketingDepartmentSerializer, 
    CompanyAchievementsSerializer,
    CompanyChallengesSerializers,
    CompanyServicesSerializer,
    CompanyPostsSerializer,
    CompanyPartnersSerializer,
    PartnersReviewsSerializer,
    CompanyApplicationSerializer,
    ApplicationFormSerializer,
    StaticPagesSerializer,
    CompanyTeamSerializer,
    CompanyAdvertisingSerializer,
    CompanyVideoReviewsSerializer,
    FAQSerializer,
    CompanyBrendingSerializer,
    CompanyFeaturesSerializer,
    VideoProductionSerializer,
    CRMServiceSerializer,
    MarketingSupportSerializer,
    ServiceOfferingSerializer,
    CompanyPostsItemsSerializer,
    CompanyPostsItemsDetailSerializer,
    BusinessTypeSerializer,
    PromotionTypeSerializer,
    )

class MarketingDepartmentView(generics.RetrieveAPIView):
    serializer_class = MarketingDepartmentSerializer
    
    def get_object(self):
        return MarketingDepartment.objects.prefetch_related(
            'chapters',
        ).first() 


class CompanyAchievementsView(generics.RetrieveAPIView):
    serializer_class = CompanyAchievementsSerializer
    
    def get_object(self):
        return CompanyAchievements.objects.prefetch_related(
            'items',
        ).first() 
    

class CompanyChallengesView(generics.RetrieveAPIView):
    serializer_class = CompanyChallengesSerializers
    
    def get_object(self):
        return CompanyChallenges.objects.prefetch_related(
            'items',
        ).first() 


class CompanyServicesView(generics.RetrieveAPIView):
    serializer_class = CompanyServicesSerializer
    
    def get_object(self):
        return CompanyServices.objects.prefetch_related(
            'items',
        ).first() 


class CompanyPostsView(generics.RetrieveAPIView):
    serializer_class = CompanyPostsSerializer
    
    def get_object(self):
        company_posts = CompanyPosts.objects.first()
        if company_posts:
            # Получаем только 3 последних записи для items, используя related_name и ordering из модели
            company_posts.items_limited = company_posts.items.all()[:3]
        return company_posts


class CompanyPartnersView(generics.RetrieveAPIView):
    serializer_class = CompanyPartnersSerializer
    
    def get_object(self):
        return CompanyPartners.objects.prefetch_related(
            'items',
        ).first() 


class PartnersReviewsView(generics.RetrieveAPIView):
    serializer_class = PartnersReviewsSerializer
    
    def get_object(self):
        return PartnersReviews.objects.prefetch_related(
            'items',
        ).first() 


class CompanyApplicationView(generics.RetrieveAPIView):
    serializer_class = CompanyApplicationSerializer
    
    def get_object(self):
        return CompanyApplication.objects.first()


class ApplicationFormView(generics.CreateAPIView):
    serializer_class = ApplicationFormSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Заявка успешно отправлена",
                    "data": serializer.data
                }, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "status": "error",
                "message": "Ошибка при отправке заявки",
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )


class StaticPagesListView(generics.ListAPIView):
    serializer_class = StaticPagesSerializer
    queryset = StaticPages.objects.all()


class StaticPagesDetailView(generics.RetrieveAPIView):
    serializer_class = StaticPagesSerializer
    lookup_field = 'slug'
    queryset = StaticPages.objects.all()




class CompanyTeamView(generics.RetrieveAPIView):
    serializer_class = CompanyTeamSerializer
    
    def get_object(self):
        return CompanyTeam.objects.prefetch_related(
            'items',
        ).first()


class CompanyAdvertisingView(generics.RetrieveAPIView):
    serializer_class = CompanyAdvertisingSerializer
    
    def get_object(self):
        return CompanyAdvertising.objects.prefetch_related(
            'items',
        ).first()


class CompanyVideoReviewsView(generics.RetrieveAPIView):
    serializer_class = CompanyVideoReviewsSerializer
    
    def get_object(self):
        return CompanyVideoReviews.objects.prefetch_related(
            'items',
        ).first()
    

class FAQView(generics.ListAPIView):
    serializer_class = FAQSerializer
    queryset = FAQ.objects.all()



class CompanyBrendingView(generics.RetrieveAPIView):
    serializer_class = CompanyBrendingSerializer
    
    def get_object(self):
        return CompanyBrending.objects.prefetch_related(
            'items',
        ).first()



class CompanyFeaturesView(generics.RetrieveAPIView):
    serializer_class = CompanyFeaturesSerializer
    
    def get_object(self):
        return CompanyFeatures.objects.prefetch_related(
            'items',
        ).first()
    

class VideoProductionView(generics.RetrieveAPIView):
    serializer_class = VideoProductionSerializer
    
    def get_object(self):
        return VideoProduction.objects.prefetch_related(
            'items',
        ).first()
    

class CRMServiceView(generics.RetrieveAPIView):
    serializer_class = CRMServiceSerializer
    
    def get_object(self):
        return CRMService.objects.prefetch_related(
            'items',
        ).first()


class MarketingSupportView(generics.RetrieveAPIView):
    serializer_class = MarketingSupportSerializer
    
    def get_object(self):
        return MarketingSupport.objects.prefetch_related(
            'items',
        ).first()


class ServiceOfferingView(generics.RetrieveAPIView):
    serializer_class = ServiceOfferingSerializer
    
    def get_object(self):
        return ServiceOffering.objects.prefetch_related(
            'items',
        ).first()


class PostsPagination(PageNumberPagination):
    page_size = 9  # количество элементов на странице
    page_size_query_param = 'page_size'
    max_page_size = 100


class CompanyPostsItemsFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name='tags__tags',
        to_field_name='tags',
        queryset=Tags.objects.all()
    )
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CompanyPostsItems
        fields = ['tags', 'title']


class CompanyPostsItemsListView(generics.ListAPIView):
    serializer_class = CompanyPostsItemsSerializer
    pagination_class = PostsPagination
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CompanyPostsItemsFilter
    search_fields = ['title', 'company_name']

    def get_queryset(self):
        return CompanyPostsItems.objects.all().order_by('-id')


class CompanyPostsItemsDetailView(generics.RetrieveAPIView):
    serializer_class = CompanyPostsItemsDetailSerializer
    queryset = CompanyPostsItems.objects.all()
    lookup_field = 'id'


class BusinessTypeListView(generics.ListAPIView):
    serializer_class = BusinessTypeSerializer
    queryset = BusinessType.objects.all()


class PromotionTypeListView(generics.ListAPIView):
    serializer_class = PromotionTypeSerializer
    queryset = PromotionType.objects.all()
