from rest_framework import serializers
from apps.site_info.models import CompanyInfo, Address, Phones, Emails, SocialNetworks


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('title', 'address')


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ('title', 'phone')


class EmailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emails
        fields = ('title', 'email')

class SocialNetworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetworks
        fields = ('logo', 'link')


class CompanyInfoSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    phones = PhonesSerializer(many=True, read_only=True)
    emails = EmailsSerializer(many=True, read_only=True)
    social_networks = SocialNetworksSerializer(many=True, read_only=True)

    class Meta:
        model = CompanyInfo
        fields = ('logo', 'description', 'whatsapp_logo', 'whatsapp_link', 'whatsapp_text', 'work_time', 'video'
                  , 'production_video', 'addresses', 'phones', 'emails', 'social_networks')
