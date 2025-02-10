from rest_framework import generics
from apps.site_info.models import CompanyInfo
from .serializers import CompanyInfoSerializer


class CompanyInfoView(generics.RetrieveAPIView):
    serializer_class = CompanyInfoSerializer
    
    def get_object(self):
        return CompanyInfo.objects.prefetch_related(
            'addresses', 'phones', 'emails', 'social_networks'
        ).first() 