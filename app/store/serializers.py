from rest_framework import serializers

from store.models import Trousers


class TrousersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trousers
        fields = '__all__'
