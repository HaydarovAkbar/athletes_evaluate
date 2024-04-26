from django.urls import path
from .views import (CompetitionCreateApi, RingCreateApi, MatchCreateApi, MatchResultCreateApi,
                    CompetitionUpdateDeleteRetrieveAPi, RingUpdateDeleteRetieveApi, MatchResultUpdateDeleteRetriveApi,
                    MatchUpdateDeleteRetriveAPI, GetRingApi)

from .routing import websocket_urlpatterns as ws_urlpatterns

urlpatterns = [
    path('competition/', CompetitionCreateApi.as_view(), name='competition'),
    path('competition/<int:pk>/', CompetitionUpdateDeleteRetrieveAPi.as_view(),
         name='cometition_update_retrieve_destroy'),
    path('ring/', RingCreateApi.as_view(), name='ring'),
    path('ring/<int:pk>/', RingUpdateDeleteRetieveApi.as_view(), name="ring_update_retrieve_destroy"),
    path('get-ring/', GetRingApi.as_view(), name="get_ring"),
    path('match/', MatchCreateApi.as_view(), name='match'),
    path('match/<int:pk>/', MatchUpdateDeleteRetriveAPI.as_view(), name='match_update_retrieve_destroy'),
    path('matchresult/', MatchResultCreateApi.as_view(), name='matchresult'),
    path('matchresult/<int:pk>/', MatchResultUpdateDeleteRetriveApi.as_view(),
         name='match_result_update_retrieve_destroy'),
]

urlpatterns += ws_urlpatterns
