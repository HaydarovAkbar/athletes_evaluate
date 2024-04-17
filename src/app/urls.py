from django.urls import path
from .views import CompetitionCreateApi, RingCreateApi, MatchCreateApi, MatchResultCreateApi
urlpatterns=[
    path('competition/', CompetitionCreateApi.as_view(), name='competition'),
    path('ring/', RingCreateApi.as_view(), name='ring'),
    path('match/', MatchCreateApi.as_view(), name='match'),
    path('matchresult/', MatchResultCreateApi.as_view(), name='matchresult'),
]