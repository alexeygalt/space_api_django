from drf_spectacular.utils import extend_schema
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from indication.models import User
from indication.serializators.user import UserSerializer, UserCreateSerializer, ChangePasswordSerializer, \
    UserUpdateSerializer


@extend_schema(
    description="Retrieve users list",
    summary="Show all users"
)
class UserListView(ListAPIView):
    """show all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(
    description="Retrieve one user",
    summary="Show one user"
)
class UserDetailView(RetrieveAPIView):
    """show  user by pk"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


@extend_schema(
    description="Creat  user",
    summary="Create one user"
)
class UserCreateView(CreateAPIView):
    """create new user"""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


@extend_schema(
    description="Update user's data",
    summary="Update user"
)
class UserUpdateView(UpdateAPIView):
    """update user data"""
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(
    description="Delete user's data",
    summary="Delete  user"
)
class UserDeleteView(DestroyAPIView):
    """delete user by pk"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@extend_schema(
    description="Update  user's password",
    summary="Password update"
)
class UpdatePassword(APIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
