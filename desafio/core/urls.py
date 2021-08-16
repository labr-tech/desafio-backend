from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

from .views import StateViewSet, CityViewSet

app_name = 'core'

router = DefaultRouter()
router.register(r'state', StateViewSet, basename='state')
router.register(r'city', CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),
]
