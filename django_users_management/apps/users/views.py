
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_users_management.apps.users.serializers import UserSerializer
from django_users_management.apps.users.models import User


class UsersView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DeleteUser(APIView):
    def delete(self, _, **kwargs):
        user = User.objects.filter(id=kwargs['id'])
        if user:
            user.delete()
            return Response({
                "message": "User deleted"
            })
        return Response({
            "message": "User not found"
        }, status=status.HTTP_404_NOT_FOUND)
