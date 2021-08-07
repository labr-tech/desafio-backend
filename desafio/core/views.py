from rest_framework import mixins, viewsets
from django_filters import rest_framework as filters

from .models import State, City
from .serializers import CitySerializer, StateSerializer
from desafio.core.filterset import StateFilter


class StateViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = StateFilter


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = ''
