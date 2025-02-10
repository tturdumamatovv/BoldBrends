from rest_framework import serializers

from ..models import Banners


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ('title', 'sub_title', 'button_text', 'image', 'is_active')
