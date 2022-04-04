from django.urls import path
from .views import CRUDUserProfileAPIView, UserLogin

urlpatterns = [
    path('login/', UserLogin.as_view(), name='user_login'),
    path('create/', CRUDUserProfileAPIView.as_view(), name='create_user_profile'),
    path('all/', CRUDUserProfileAPIView.as_view(), name='get_all_users_profile')

]