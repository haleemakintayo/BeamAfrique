# api/urls.py
from django.urls import path
from .views import (
    ProtectedView,ContentUploadView,
    MagazineUploadView,MagazineListView,
    SignupView,SendEmailView,
    DeleteContentView,DeleteMagazineView
    )

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('upload/', ContentUploadView.as_view(), name='content_upload'),
    path('magazine/', MagazineUploadView.as_view(), name='magazine_upload'),
    path('magazines/', MagazineListView.as_view(), name='magazine-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('send-email', SendEmailView.as_view(), name='send-mail'),
    path('upload/<int:pk>/', DeleteContentView.as_view(), name='delete-content'),
    path('magazine/<int:pk>/', DeleteMagazineView.as_view(), name='delete-magazine'),
    
]
