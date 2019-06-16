from django.db import models

# Create your models here.

class Size(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre}"

class TipoPlato(models.Model):
    nombre = models.CharField(max_length=30)
    tipo_plato = models.ForeignKey("TipoPlato", null=True, blank=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_tipos_plato")

    def __str__(self):
        txtTipoPlato = self.tipo_plato if self.tipo_plato is not None else ""
        return f"{self.nombre} {txtTipoPlato}"

class Plato(models.Model):
    nombre = models.CharField(max_length=20)
    tipo_plato = models.ForeignKey(TipoPlato, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_tipos_plato")
    adiciones = models.ManyToManyField("Plato", through='Adicion')
    sizes = models.ManyToManyField(Size, through='PlatoSize')

    def __str__(self):
        return f"{self.nombre} {self.tipo_plato}"

class Adicion(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_platos")
    adicion = models.ForeignKey(Plato, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_adiciones")

    def __str__(self):
        return f"{self.plato} {self.adicion}"

class PlatoSize(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_platos")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="sizes")

    def __str__(self):
        return f"{self.plato} {self.size}"

class Menu(models.Model):
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20)
    platos_sizes = models.ManyToManyField(PlatoSize, through='MenuPlatoSize')

    def __str__(self):
        return f"Menu {self.id} {self.fecha_inicio} {self.fecha_cierre} {self.estado}"

class MenuPlatoSize(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="menus")
    plato_size = models.ForeignKey(PlatoSize, on_delete=models.CASCADE, related_name="platos_sizes")
    precio = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.menu} {self.plato_size} {self.precio}"
