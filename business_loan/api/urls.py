from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('business/', BusinessDetailsView.as_view()),
    path('loans/', LoanApplicationView.as_view()),
    path('profile/exists/', ProfileExistsView.as_view()),
    path('business/exists/', BusinessExistsView.as_view()),
]
