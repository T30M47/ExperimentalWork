# Benchmark report - Teo Matijašić

---

## Sažetak testiranog koncepta

---

U ovom benchmarku je testiran koncept konkateniranog (složenog indeksa). To je indeks na tablici u bazi podataka koji uključuje više od jednoga stupca te služi za brže pretraživanje podataka. Time, umjesto da se kreira na jednome stupcu kao i obični indeks, konkatenirani indeks se kreira na više stupaca tablice. Time, ako bi imali tablicu sa stupcima prezime i ime te ako bi često postavljali upite koji uključuju filtriranje po tim stupcima konkatenirani indeks s tim stupcima može poboljšati efikasnost upita. Sami stupci se mogu pojaviti u bilo kojem poretku unutar indeksa, ali da bi se postigla veća efikasnost upiti moraju referencirati sve ili vodeći dio stupaca. Tako bi konkatenirani indeks s stupcima (prezime, ime) mogao efikasno pronaći rezultat upita s određenim prezimenom ili s prezimenom i imenom, ali ne i samo s imenom. Općenito pravilo je da se u konkatenirani indeks prvo stavljaju stupci kojima se najčešće pristupa.

### Kako i Zašto poboljšava sustav?

* kao i običan indeks, konkatenirani indeks služi za brzi pronalazak podataka
* poboljšava sustav jer prvenstveno služi za optimizaciju upita koji uključuju više stupaca
* zbog pohrane kombinacije stupaca, potrebno je manje čitanja na disk od traženja po cijeloj tablici

### Potencijalni problemi s konkateniranim indeksom uključuju:
* veliku ovisnost o prisutnosti određenih stupaca pa odbacivanje određenih stupaca u upitu mogu dovesti do smanjena efikasnosti
* može dovesti do opterećenja održavanja ako uključuje puno stupaca
* dovodi do sporijeg ažuriranja podataka zbog toga što se i on sam treba ažurirati kada se ovisni podaci promijene.
  
Konkatenirani indeks može pridonijeti u različitim vrstama aplikacija i slučajevima korištenja. <br>
### Neki od primjera korištenja:
* kada želimo raditi pretragu po više stupaca, na primjer u online trgovinama kada želimo filtrirati proizvode po kategoriji i cijeni.
* aplikacije za praćenje transakcija gdje možemo sortirati transakcije po datumu, količini i sl.
* aplikacije za rezervacije, pronalazak dostupnih soba/stolova prema datumu, lokaciji
* geoprostorni podaci, upiti koji uključuji i zemljopisnu širinu i dužinu

## Arhitektura sustava

---

![Arhitektura sustava](system_archit.png)

Sam sustav sam implementirao kroz Django web aplikaciju. Kada stvorimo django web aplikaciju s naredbom:
```
django-admin startproject mysite
```
automatski s njom dolazi ugrađeni development web server te SQLite implementacija baze podataka. Unutar baze podataka, sam pomoću modela kreirao različite tablice (11 tablica, no na slici je prikazano samo 9 zbog preglednosti te nedostaju ProizvodSIndeksomDatum i ProizvodSIndeksomVelikaKardDatum) koje su predstavljale tablice s isto definiranim stupcima. Jedna od razlika među tablicama je ta što sam kreirao različite vrste indeksa nad njima što se vidi iz same slike. Osim toga tablice su imale različita svojstva ovisno o potrebnim usporedbama pa su tako neke tablice imale manji broj redaka, a druge veći broj, neke su imale velike kardinalnosti odabranih stupaca, a neke manje te su neke služile za upite samo nad pojedinim stupcima dok su druge služile za postavljanje upita nad svim stupcima. 

Same testove sam provodio slanjem ab testova na odgovarajuće URL-ove koji su pokretali određene funkcije u kojima sam implementirao da pokreću ab naredbu i ispišu njen rezultat. 
Ti ab testovi su zapravo bili slani na URL koji su pokretali poglede (views) unutar Django web aplikacije koji su bili zaduženi za postavljanje upita nad odgovarajućom tablicom unutar baze podataka. Time, ako je URL sadržavao /withoutIndex, upit se postavljao na tablicu ProizvodBezIndeksa, ako je sadržavao /withIndeks na tablicu ProizvodSIndeksom itd. Može se vidjeti i da je URL-ova više nego tablica jer su zadnja dva služila za slanje upita sa samo dijelom stupaca, a ne svim stupcima na već postojeću tablicu.

Web Server unutar Django web aplikacije ne komunicira direktno s bazom podataka jer on služi samo za vraćanje statičnih odgovora pa je time GET (SELECT) upit na određeni URL prvo došao do web servera (Django development server) koji ga je onda proslijedio do aplikacijskog servera ili same Django aplikacije gdje su se onda pregledavali URL-ovi, pozivali određeni pogledi te time i odgovarajuće tablice i tu se onda provodilo objektno-relacijsko preslikavanje (ORM). 

Upiti na svaku tablicu su izgledali otprilike jednako te je njihov generalni pseudokod prikazan na dnu slike (Većinom su bili slani upiti na sve stupce koji su bili sadržani u indeksu, jedino se kod usporedbe dobrog i krivog indeksa slao upit na prva dva stupca, naziv i cijenu). Kod slanja određenih URL-ova, osim odgovarajuće putanje, dodani su i parametri sa znakom upitnika koji su bili odvojeni znakom & te su oni predstavljali vrijednosti stupaca (/?naziv=name&cijena=price&datum_kreiranja=date). 

## Simulacija podataka 

---

Same podatke sam simulirao pomoću factory-boy-a i Faker-a koji služe za kreiranje lažnih podataka. U sve tablice sam  točno 100000 podataka, osim kod onih s oznakom "ManjeRedaka" te sam kod njih postavio 100 podataka. Kako sam kreirao indekse nad stupcima naziv, cijena i datum_kreiranja upite sam većinom provodio nad njima. 

Kako bi usporedio i prikazao razliku i performanse pojednih vrsta konkateniranih indeksa, većinom sam uspoređivao dvije po dvije situacije od ukupno četiri.
Time sam prvo generirao jednu tablicu s normalnim indeksom gdje je bilo 100 podataka i drugu tablicu bez indeksa sa 100 podataka s istim kardinalnostima svih stupaca kako bi tablice bile jednake. Tu mi je bio cilj pokazati kako indeks nema efekta kada je u tablicama jako malo redaka. Zatim sam kreirao iste dvije tablice samo s 100000 podataka kako bi tu pokazao da kod puno podataka indeks počinje poboljšavati performanse.

Zatim, kako bi usporedio potpuni i djelomični indeks, kreirao sam tri nove tablice sa 100000 podataka. Prva je imala potpuni indeks i veliku kardinalnost stupaca naziv i cijena koji su bili sadržani u djelomičnom indeksu. Druge dvije tablice su imale djelomični indeks samo na stupcima naziv i cijena samo s drugačijim kardinalnostima stupaca naziv i cijene. Tu mi je bio cilj pokazati kako kardinalnost stupaca koji su sadržani u djelomičnom indeksu imaju utjecaja na performanse upita s obzirom na obični indeks.

Na kraju sam, kako bi testirao potpuni i indeks u krivom redoslijedu krerirao još četiri nove tablice. Prve dvije su imale indeks nad svim stupcima u normalnom redoslijedu te veliku i malenu kardinalnost stupaca naziv i cijena nad kojima se izvodio upit. Druge dvije su imale indekse nad svim stupcima u krivom redoslijedu te velike i malene kardinalnosti stupaca naziv i cijena. Tu je bila razlika što sam postavljao upit samo nad stupcima naziv i cijena kako bi prikazao performanse upita s krivim indeksom ovisno i njihovoj kardinalnosti.

Testirao sam i vremena odgovora s ispravnim i krivim indeksom kada koristimo upit nad svim stupcima.

**Primjer generiranja lažnih podataka za jednu tablicu:**

```
class Proizvod_KriviIndeks_VelikaKard_Factory(DjangoModelFactory):
    class Meta:
        model = Proizvod_KriviIndeks_VelikaKard

    naziv = factory.Faker("word")
    opis = factory.Faker("sentence", nb_words = 10)
    cijena = factory.Faker("pydecimal", left_digits=random.choice([1, 2, 3]), right_digits=2, positive = True)
    dostupna_kolicina = factory.fuzzy.FuzzyInteger(0, 999)
    datum_kreiranja = factory.Faker('date_time')
    datum_azuriranja = factory.Faker('date_time')
```

## Mjerenja vremena odgovora

---

Za mjerenja vremena odgovora sam koristio Apache Benchmark (ab). Radi lakšeg pokretanja testova, napravio sam jednostavan GUI s gumbima koji automatski pokreću ab test te prikazuju rezultat testa. Te ab naredbe sam hard-codirao unutar koda, ali sam i napisao upute kako slati vlastite ab testove.
Što se tiče same ab naredbe, na svim testovima sam koristio istu verziju:
```
ab -n 1000 -c 3 "URL"
```
Time sam definirao da se pošalje 1000 zahtjeva te da bude razina konkurencije 3, odnosno da se šalju tri istovremena zahtjeva. Razlog zbog kojega sam slao samo 1000 zahtjeva je bio veliki broj različitih usporedbi pa bi testovi predugo trajali, a ovako se relativno mogu brzo testirati i, još bitnije, prikazati razlike. Razinu konkurencije sam postavio na 3 jer mi na početnim testiranjima, bez konkurencije nije bilo previše razlike pa sam odlučio da se šalju tri istovremena zahtjeva.
Kod rezultata sam za tri testiranja za svaku usporedbu promatrao prosjek vremena po konkurentnim zahtjevima te 95. percentil kako bi potvrdio rezultate dobivene prosjekom jer oni mogu biti nepouzdani. Taj 95. Percentil je definirao da je 95% zahtjeva imalo vrijeme odgovora manje ili jednako od dobivenog praga u milisekundama.  

## Rezultati i grafovi

---

### Usporedba korištenja indeksa i korištenja potpunog indeksa na upite sa svim stupcima iz indeksa ovisno o veličini tablice

### Usporedba korištenja potpunog i djelomičnog indeksa na upite sa svim stupcima iz indeksa ovisno o kardinalnosti atributa sadržanih u djelomičnom indeksu

### Usporedba korištenja potpunog i indeksa u krivom redoslijedu na upite samo s prva dva stupca iz točnog indeksa ovisno o njihovoj kardinalnosti

### Usporedba korištenja potpunog i indeksa u krivom redoslijedu na upite sa svim stupcima iz indeksa
