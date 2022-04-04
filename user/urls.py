from django.urls import path
from .views import CRUDUserProfileAPIView

urlpatterns = [
    path('create/', CRUDUserProfileAPIView.as_view(), name='create_user_profile'),
    path('all/', CRUDUserProfileAPIView.as_view(), name='get_all_users_profile')

]