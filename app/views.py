
from django.shortcuts import render
from .models import Tariflar,Header,Navbar
from .serializers import TarifSerializer,HeaderSerializer,NavbarSerializer
from rest_framework.viewsets import ModelViewSet


class TariflarView(ModelViewSet):
    queryset = Tariflar.objects.all()
    serializer_class = TarifSerializer
    

class HeadersView(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
   

class NavbarView(ModelViewSet):
    lis = []
    all = Navbar.objects.all()
    for i in all:
        lis.append(i.id)
    lis = max(lis)
    for dele in all:
        if dele.id != lis:
            dele.delete()
    queryset = Navbar.objects.filter(id = lis)
    serializer_class = NavbarSerializer