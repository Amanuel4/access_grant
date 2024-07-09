from rest_framework import serializers
from . models import *


class AccessGrantTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessGrantTable
        fields = '__all__'







