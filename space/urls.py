from django.urls import path, include
from rest_framework import routers

from space.views import StationViewSet, StationCreateView

space_router = routers.SimpleRouter()
space_router.register('stations', StationViewSet)
urlpatterns = [
    path("", include(space_router.urls)),
    path("stations/<int:pk>/state/", StationCreateView.as_view()),


]
