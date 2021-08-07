from desafio.filterset import SearchFilterSet

from .models import State


class StateFilter(SearchFilterSet):

    class Meta:
        model = State
        fields = ['q']
        search_fields = ['code__icontains', 'name__icontains']
