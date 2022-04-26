


from django.contrib import admin
from .models import Loty, Kraje, Linie

class LinieAdmin(admin.ModelAdmin):
    list_display = ['nazwa_linii', 'rodzaj_linii']

admin.site.register(Linie, LinieAdmin)

class LotyAdmin(admin.ModelAdmin):
    list_display = ['lotnisko_wylot', 'lotnisko_przylot', 'data_lotu', 'kraj','linia']
    list_filter = ['data_lotu', 'kraj']
    search_fields = ['linia']

admin.site.register(Loty, LotyAdmin)


class KrajeAdmin(admin.ModelAdmin):
    list_display = ['nazwa_kraju', 'kontynent']

admin.site.register(Kraje, KrajeAdmin)