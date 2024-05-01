from django.urls import path
from .views import (CompetitionCreateApi, RingCreateApi, MatchCreateApi, MatchResultCreateApi,
                    CompetitionUpdateDeleteRetrieveAPi, RingUpdateDeleteRetieveApi, MatchResultUpdateDeleteRetriveApi,
                    MatchUpdateDeleteRetriveAPI, GetRingApi, GetMatchResultApi, PatchMatchResultApi, GetActiveMatchApi, ChangeMatchStatusApi)

# from .routing import websocket_urlpatterns as ws_urlpatterns

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
    path('referee-match-result/<int:pk>/', PatchMatchResultApi.as_view(), name='referee_match_result'),
    path('get-referee-match-result/', GetMatchResultApi.as_view(), name='referee_match_result'),
    path('get-active-match-result', GetActiveMatchApi.as_view(), name='get_active_match_result'),
    path('change-match-status/<int:pk>/', ChangeMatchStatusApi.as_view(), name='change_match_status'),
]

# urlpatterns += ws_urlpatterns
