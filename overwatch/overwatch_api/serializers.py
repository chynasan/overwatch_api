from overwatch.overwatch_api.models import Hero, Role, Maps
from rest_framework import serializers


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ['Name', 'Description', 'Health', 'Abilities', 'Role']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['Name', 'PassiveAbility']

class MapsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Maps
        fields = ['Name', 'Description']