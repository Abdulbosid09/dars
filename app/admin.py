from django.contrib import admin
from .models import Header, Navbar,Tariflar


admin.site.register(Navbar)

admin.site.register(Tariflar)

admin.site.register(Header)