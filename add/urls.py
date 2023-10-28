from django.urls import path,include
from .views import get_ads_by_location, create_ad, delete_ad,update_ad,LocationListView,LocationDetailView
from .views import DailyVisitorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'visitors', DailyVisitorViewSet)
urlpatterns = [
    path('ads/<str:location_keyword>/', get_ads_by_location, name='ads-by-location'),
    path('ads/create/', create_ad, name='ads-create'),
    path('ads/del/<int:pk>/', delete_ad, name='ad-delete'),
    path('ads/update/<int:pk>/', update_ad, name='ad-update'),
    path('locations/add/', LocationListView.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    path('', include(router.urls)),
]
