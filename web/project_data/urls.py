from django.urls import path
from .views import kickstarter_detail_view, kickstarter_list_view


urlpatterns = [
    path('', kickstarter_list_view, name='home'),
    path('<int:pk>', kickstarter_detail_view, name='kickstarter_details'),
]
