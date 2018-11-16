from rest_framework import generics

from user.models import Role, User
from user.serializers import RoleSerializer, UserSerializer


class RoleList(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    def get_queryset(self):
        return Role.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def post(self, request):
    #     Course.objects.create(
    #         name=request.POST.get('name'),
    #         description=request.POST.get('description'),
    #         logo = request.POST.get('logo'))


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def post(self, request):
    #     Course.objects.create(
    #         name=request.POST.get('name'),
    #         description=request.POST.get('description'),
    #         logo = request.POST.get('logo'))


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class RoleDetail(generics.ListCreateAPIView):
    queryset = User.objects.filter(roleid=1)
    serializer_class = RoleSerializer


class UserDetail(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer