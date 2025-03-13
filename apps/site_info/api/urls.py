from django.urls import path
from .views import CompanyInfoView, email_verify

urlpatterns = [
    path('company-info/', CompanyInfoView.as_view(), name='company-info'),
    path('email_verify/', email_verify, name='email_verify'),
]
