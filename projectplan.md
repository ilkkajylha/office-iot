# Projektisuunnitelma


## Johdanto

Innovaatioprojekti-kurssilla pääsimme toteuttamaan IOT-projektia Martelalle, jossa tarkoituksena on luoda laite Arduino-mikrokontrollerin ja Raspberry pi -minitietokoneen avulla helpottamaan toimitilojen käyttöä ja varausta.

## Mitä tehdään

Prototyyppi, joka tunnistaa passiivisen infrapunasensorin avulla onko huoneessa  ihmisiä ja lähettää siitä tietoa eteenpäin käyttäen Raspberry pi:tä.
Kyseessä on prototyyppi, joten valmistuva laite ei sellaisenaan sovellu massatuotettavaksi.

Projektin aikana myös julkaistaan säännöllisesti [https://officeiot.wordpress.com/](blogikirjoituksia), jotta molemmat osapuolet saavat näkyvyyttä jo työskentelyvaiheessa sekä projektin jälkeen.

## Lisenssi

Olemme sopineet, että käytämme MIT-lisenssiä, jolloin molemmat osapuolet voivat käyttää lopputuotetta haluamallaan tavalla, kunhan lisenssi ja sen osapuolet mainitaan. https://opensource.org/licenses/MIT 

## Komponentit

* [https://www.arduino.cc](Arduino)
* [https://www.raspberrypi.org/](Raspberry Pi)
* Passiivinen infrapunasensori

## Teknologiat

* [https://www.vagrantup.com/](Vagrant) - yhtenäisiin testaus- ja kehitysympäristöihin
* [https://kanbanflow.com](KanbanFlow) - ketterään projektinhallintaan
* [https://en.wikipedia.org/wiki/Internet_Relay_Chat](IRC) - kommunikointiin
* [https://git-scm.com/](Git) - versionhallintaan

## Aikataulu

### Viikko 39 (21.9.-27.9.)
* Blogipostaus julkiseksi
* Arduinon ja Raspberry pi:n välinen kommunikointi

### Viikko 40 (28.-9.-4.10.)
* Blogipostaus julkiseksi
* Datan lähetys Raspberry pi:ltä 
### Viikko 41 (5.10.-11.10.)
* Blogipostaus julkiseksi
* Eri komponenttien keskinäinen toiminta, arkkitehtuuri, määritelty
### Viikko 42 (12.10.-18.10.)
* Blogipostaus julkiseksi
* Datan vastaanotto raspberry pi:ltä, backend. 
* frontend demo
### Viikko 43 (19.10.-25.10.)
* Blogipostaus julkiseksi
* Visuaalisempi frontend
### Viikko 44 (26.10.-1.11.)
* Blogipostaus julkiseksi
* 3D tulostetun kotelon esiversio
### Viikko 45 (2.11.-8.11.)
* Blogipostaus julkiseksi
* Bugien metsästystä ja refaktorointia
### Viikko 46 (9.11.-15.11.)
* laitteen testaus oikeassa ympäristössä
### Viikko 47 (16.11.-22.11.)
* Blogipostaus julkiseksi
* Valmis prototyyppi(?)
### Viikko 48 (23.11.-29.11.)
* Blogipostaus julkiseksi
### Viikko 49 (30.11.-6.12.)
* Blogipostaus julkiseksi
### Viikko 50 (7.12.-13.12.)
* Valmiin projektin esittely Haaga-Heliassa (keskiviikkona 9.12.?)


## Tekijät:

### Ilkka Jylhä
* Arduino ja Raspberry pi:llä ajettavan koodin kirjoittaminen ja suunnittelu.
### Antti Salo
* Käyttöliittymän suunnittelu ja koodaus. Kotelon suunnittelu ja 3D mallintaminen. 
### Sami Nisonen
* Dokumentointi ja avustavia tehtäviä suunnittelussa ja koodin kirjoittamisessa

