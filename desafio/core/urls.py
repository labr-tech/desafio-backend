from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

from .views import StateViewSet

app_name = 'core'

router = DefaultRouter()
router.register(r'state', StateViewSet, basename='state')

urlpatterns = [
    path('', include(router.urls)),
]
