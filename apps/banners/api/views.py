from rest_framework.generics import ListAPIView

from ..models import Banners
from .serializers import BannersSerializer


class BannersView(ListAPIView):
    queryset = Banners.objects.filter(is_active=True)
    serializer_class = BannersSerializer
