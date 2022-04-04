from django.urls import path
from .views import CRUDTutorialAPiView

urlpatterns = [
    path('create/', CRUDTutorialAPiView.as_view(), name='create_tutorial'),
    path('all/', CRUDTutorialAPiView.as_view(), name='get_all_tutorials'),
    path('<str:uuid>/', CRUDTutorialAPiView.as_view(), name='get_single_tutorial'),
    path('<str:uuid>/update/', CRUDTutorialAPiView.as_view(), name='get_single_tutorial')

]