from django.contrib.auth.models import User
from rest_framework import serializers

from app.models import Plate, Bid

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email','password', 'is_staff')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plate
        fields = "__all__"

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"
