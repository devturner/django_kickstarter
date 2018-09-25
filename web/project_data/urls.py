from django.urls import path
from .views import campaign_detail_view, campaigns_list_view


urlpatterns = [
    path('', campaigns_list_view, name='campaign_list'),
    path('<int:pk>', campaign_detail_view, name='campaign_detail'),
]
