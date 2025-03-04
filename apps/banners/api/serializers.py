from rest_framework import serializers
from apps.banners.models import Banners, BannerText


class BannerTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerText
        fields = ('text', 'link')


class BannersSerializer(serializers.ModelSerializer):
    banner_text = BannerTextSerializer(source='bannertext', read_only=True)

    class Meta:
        model = Banners
        fields = ('title', 'sub_title', 'button_text', 'image', 'is_active', 'banner_text')
