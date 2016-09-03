from rest_framework import serializers

from .models import DatastoreUser
from djangae.contrib.gauth.datastore.models import Group

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DatastoreUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'groups', 'password', 'url')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = DatastoreUser(first_name=validated_data['first_name'],
                                last_name=validated_data['last_name'],
                                username=validated_data['username'],
                                email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'url')
