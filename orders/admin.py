from django.contrib import admin

from .models import Size, TipoPlato, Plato, Adicion, PlatoSize, Menu, MenuPlatoSize
# Register your models here.
admin.site.register(Size)
admin.site.register(TipoPlato)
admin.site.register(Plato)
admin.site.register(Adicion)
admin.site.register(PlatoSize)
admin.site.register(Menu)
admin.site.register(MenuPlatoSize)
