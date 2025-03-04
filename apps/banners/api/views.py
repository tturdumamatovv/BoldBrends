from rest_framework.generics import ListAPIView

from ..models import Banners
from .serializers import BannersSerializer


class BannersView(ListAPIView):
    serializer_class = BannersSerializer
    
    def get_queryset(self):
        return Banners.objects.filter(is_active=True).select_related('bannertext')
