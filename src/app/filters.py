from django_filters import rest_framework as filters
from .models import Competition

class AcriveCompetitionFilter(filters.FilterSet):
    # is_active=filters.BooleanFilter(field_name='is_active', lookup_expr='True')

    class Meta:
        model=Competition

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.order_by('-created_at')