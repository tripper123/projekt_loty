from django.db import models


# class Rok(models.Model):
#     data_lotu = models.CharField(max_length=32),
#     lotnisko_wylotu = models.CharField(max_length=32),
#     lotnisko_przylotu = models.CharField(max_length=32)

#     def __str__(self):
#         return {self.id} , {self.lotnisko_wylotu} , {self.lotnisko_przylotu}
# # Create your models here.
#
class Linie(models.Model):
    STATUS_CHOICES =( ('', ''), ('niskokosztowa','Niskokosztowa'), ('tradycyjna', 'Tradycyjna'), ('czarterowa', 'Czarterowa'))
    nazwa_linii = models.CharField(max_length=32)
    rodzaj_linii = models.CharField(max_length=32, choices=STATUS_CHOICES, blank=True, null=True, default='')
    def __str__(self):
        return f'{self.nazwa_linii}'
    class Meta:
        verbose_name="Linia"
        verbose_name_plural="Linie"

class Kraje(models.Model):
    STATUS_CHOICES = (
    ('', ''), ('europa', 'Europa'), ('azja', 'Azja'),('afryka', 'Afryka'), ('ameryka południowa', 'Ameryka Południowa'),('australia', 'Australia'), \
    ('ameryka północna', 'Ameryka Północna'))
    nazwa_kraju = models.CharField(max_length=32)
    kontynent = models.CharField(max_length=32, choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.nazwa_kraju}'

    class Meta:
        verbose_name="Kraj"
        verbose_name_plural="Kraje"

class Loty(models.Model):
    lotnisko_wylot = models.CharField(max_length=32)
    lotnisko_przylot = models.CharField(max_length=32)
    data_lotu = models.DateField(max_length=32)
    kraj = models.ForeignKey(Kraje, on_delete=models.PROTECT, blank=True, null=True)
    linia = models.ForeignKey(Linie, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):

        return f'{self.lotnisko_wylot} {self.lotnisko_przylot} {self.data_lotu} {self.kraj} {self.linia}'

    class Meta:
        verbose_name="Lot"
        verbose_name_plural="Loty"
