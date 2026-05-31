from django.contrib import admin

from .models import Adocao, Adotante, Animal, Tratamento

admin.site.register(Animal)
admin.site.register(Tratamento)
admin.site.register(Adotante)
admin.site.register(Adocao)
