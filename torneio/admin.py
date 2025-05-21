from django.contrib import admin
from .models import Treinador, Pokemon, Batalha, Item, Time, Local, TreinadorTime

admin.site.register(Treinador)
admin.site.register(Pokemon)
admin.site.register(Batalha)
admin.site.register(Item)
admin.site.register(Time)
admin.site.register(Local)
admin.site.register(TreinadorTime)
