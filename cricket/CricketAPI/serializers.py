from rest_framework import serializers
from players.models import Players

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = "__all__"