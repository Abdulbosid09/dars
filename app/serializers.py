from rest_framework import serializers

from .models import Tariflar,Header,Navbar

class TarifSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariflar
        fields = '__all__'


class HeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Header
        fields = '__all__'

class NavbarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Navbar
        fields = '__all__'

