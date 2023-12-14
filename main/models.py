from django.db import models

# Create your models here.


class Proizvod_bezIndeksa(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_SIndeksom(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena', 'datum_kreiranja'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_DioIndeksa(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_KriviIndeks(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['datum_kreiranja', 'cijena', 'naziv'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_bezIndeksa_MaloRedaka(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_SIndeksom_MaloRedaka(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena', 'datum_kreiranja'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_SIndeksom_VelikaKard(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena', 'datum_kreiranja'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_DioIndeksa_VelikaKard(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_KriviIndeks_VelikaKard(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['datum_kreiranja', 'cijena', 'naziv'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"

class Proizvod_SIndeksom_Datum(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena', 'datum_kreiranja'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"
    
class Proizvod_SIndeksom_VelikaKard_Datum(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    dostupna_kolicina = models.PositiveIntegerField(default=0)
    datum_kreiranja = models.DateField()
    datum_azuriranja = models.DateField()

    class Meta:
          indexes = [models.Index(fields=['naziv', 'cijena', 'datum_kreiranja'])]

    def __str__(self):
        return f"{self.naziv} - ${self.cijena}"