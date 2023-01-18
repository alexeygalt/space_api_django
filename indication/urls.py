from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from indication.views.user import *

from indication.views.indication import *

urlpatterns = [
    path("users/", UserListView.as_view()),
    path("users/<int:pk>", UserDetailView.as_view()),
    path("users/create/", UserCreateView.as_view()),
    path("users/password/", UpdatePassword.as_view()),
    path("users/<int:pk>/update/", UserUpdateView.as_view()),
    path("users/<int:pk>/delete/", UserDeleteView.as_view()),
    path('users/token/', TokenObtainPairView.as_view()),
    path('users/token/refresh/', TokenRefreshView.as_view()),
    path('indications/', IndicationListView.as_view()),
    path("indications/<int:pk>", IndicationDetailView.as_view()),
    # path("stations/<int:pk>/create/", IndicationCreateView.as_view()),
]
