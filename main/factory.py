## factories.py
import factory
import factory.fuzzy
import random
from factory.django import DjangoModelFactory

from main.models import *

## Defining a factory
cijena_values = [round(random.uniform(1, 1000), 2) for _ in range(2000)]

class Proizvod_BezIndeksaFactory(DjangoModelFactory):
    class Meta:
        model = Proizvod_bezIndeksa

    naziv = factory.Iterator(["bread", "eggs", "milk"])
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Iterator([1.99, 9.99, 2.99])
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_SIndeksomFactory(DjangoModelFactory):
    class Meta:
        model = Proizvod_SIndeksom

    naziv = factory.Iterator(["bread", "eggs", "milk"])
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Iterator([1.99, 9.99, 2.99])
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_DioIndeksaFactory(DjangoModelFactory):
    class Meta:
        model = Proizvod_DioIndeksa

    naziv = factory.Iterator(["bread", "eggs", "milk"])
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Iterator([1.99, 9.99, 2.99])
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_KriviIndeksFactory(DjangoModelFactory):
    class Meta:
        model = Proizvod_KriviIndeks

    naziv = factory.Sequence(lambda n: f'proizvod_{n % 2000}')
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Sequence(lambda n: cijena_values[n % 2000])
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_BezIndeksa_MaloRedaka_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_bezIndeksa_MaloRedaka
    
    naziv = factory.Iterator(["bread", "eggs", "milk"])
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Iterator([1.99, 9.99, 2.99])
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_SIndeksom_MaloRedaka_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_SIndeksom_MaloRedaka

    naziv = factory.Iterator(["bread", "eggs", "milk"])
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Iterator([1.99, 9.99, 2.99])
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_DioIndeksa_VelikaKard_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_DioIndeksa_VelikaKard

    naziv = factory.Faker("word")
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Faker("pydecimal", left_digits=random.choice([1, 2, 3]), right_digits=2, positive = True)
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_KriviIndeks_VelikaKard_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_KriviIndeks_VelikaKard

    naziv = factory.Faker("word")
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Faker("pydecimal", left_digits=random.choice([1, 2, 3]), right_digits=2, positive = True)
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_SIndeksom_VelikaKard_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_SIndeksom_VelikaKard

    naziv = factory.Faker("word")
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Faker("pydecimal", left_digits=random.choice([1, 2, 3]), right_digits=2, positive = True)
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')    

class Proizvod_SIndeksom_Datum_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_SIndeksom_Datum
    
    naziv = factory.Sequence(lambda n: f'proizvod_{n % 2000}')
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Sequence(lambda n: cijena_values[n % 2000])
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')

class Proizvod_SIndeksom_VelikaKard_Datum_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_SIndeksom_VelikaKard_Datum

    naziv = factory.Faker("word")
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Faker("pydecimal", left_digits=random.choice([1, 2, 3]), right_digits=2, positive = True)
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')