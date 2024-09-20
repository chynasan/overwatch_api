
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from overwatch.overwatch_api.serializers import HeroSerializer, RoleSerializer, MapsSerializer
from overwatch.overwatch_api.models import Hero, Role, Maps


class HeroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows heroes to be viewed or edited.
    """
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]


class MapsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Maps.objects.all()
    serializer_class = MapsSerializer
    permission_classes = [permissions.IsAuthenticated]