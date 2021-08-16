from desafio.filterset import SearchFilterSet

from .models import State, City


class StateFilter(SearchFilterSet):

    class Meta:
        model = State
        fields = ['q']
        search_fields = ['code__icontains', 'name__icontains']


class CityFilter(SearchFilterSet):
    class Meta:
        model = City
        fields = ['q']
        search_fields = [
            'name__icontains',
            'slug__icontains',
            'state__code__icontains',
            'state__name__icontains'
        ]
