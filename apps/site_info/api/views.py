from rest_framework import generics
from apps.site_info.models import CompanyInfo
from .serializers import CompanyInfoSerializer

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .utils import decode_token

class CompanyInfoView(generics.RetrieveAPIView):
    serializer_class = CompanyInfoSerializer
    
    def get_object(self):
        return CompanyInfo.objects.prefetch_related(
            'addresses', 'phones', 'emails', 'social_networks'
        ).first() 


@api_view(['GET'])
def email_verify(request):
    token = request.GET.get('token')
    if token is None:
        return Response({"error": "Token is missing"}, status=status.HTTP_400_BAD_REQUEST)

    # Верификация токена
    try:
        # Пример декодирования токена (зависит от вашей логики)
        decoded_token = decode_token(token)
        user_id = decoded_token.get('user_id')
        user = User.objects.get(id=user_id)

        # Обновляем статус пользователя на 'verified'
        user.is_active = True
        user.save()

        return Response({"message": "Email verified successfully!"}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": f"Verification failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)