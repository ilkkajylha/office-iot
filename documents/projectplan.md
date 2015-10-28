# Projektisuunnitelma


## Johdanto

Innovaatioprojekti-kurssilla pääsimme toteuttamaan IOT-projektia Martelalle, jossa tarkoituksena on luoda laite Arduino-mikrokontrollerin ja Raspberry pi -minitietokoneen avulla helpottamaan toimitilojen käyttöä ja varausta.

## Mitä tehdään

Prototyyppi, joka tunnistaa passiivisen infrapunasensorin avulla onko huoneessa  ihmisiä ja lähettää siitä tietoa eteenpäin käyttäen Raspberry pi:tä.
Kyseessä on prototyyppi, joten valmistuva laite ei sellaisenaan sovellu massatuotettavaksi.

Projektin aikana myös julkaistaan säännöllisesti [blogikirjoituksia](https://officeiot.wordpress.com/), jotta molemmat osapuolet saavat näkyvyyttä jo työskentelyvaiheessa sekä projektin jälkeen.

## Lisenssi

Olemme sopineet, että käytämme MIT-lisenssiä, jolloin molemmat osapuolet voivat käyttää lopputuotetta haluamallaan tavalla, kunhan lisenssi ja sen osapuolet mainitaan. https://opensource.org/licenses/MIT 

## Komponentit

* [arduino](https://www.arduino.cc)
* [Raspberry Pi](https://www.raspberrypi.org)
* Passiivinen infrapunasensori

## Teknologiat

* [Vagrant](https://www.vagrantup.com/) - yhtenäisiin testaus- ja kehitysympäristöihin
* [Kanbanflow](https://kanbanflow.com) - ketterään projektinhallintaan
* [IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) - kommunikointiin
* [Git](https://git-scm.com/) - versionhallintaan

## Aikataulu

### Viikko 39 (21.9.-27.9.)
* Arduinon ja Raspberry pi:n välinen kommunikointi
* [Make arduino talk to python](https://officeiot.wordpress.com/2015/10/01/make-arduino-talk-to-python/)
* [How to debug serial port](https://officeiot.wordpress.com/2015/09/30/how-to-debug-serial-port/)

### Viikko 40 (28.-9.-4.10.)
* Datan lähetys Raspberry pi:ltä 

### Viikko 41 (5.10.-11.10.)
* Eri komponenttien keskinäinen toiminta, arkkitehtuuri, määritelty

### Viikko 42 (12.10.-18.10.)
* Datan vastaanotto raspberry pi:ltä, backend. 
* frontend demo

### Viikko 43 (19.10.-25.10.)
* Visuaalisempi frontend

### Viikko 44 (26.10.-1.11.)
* 3D tulostetun kotelon esiversio

### Viikko 45 (2.11.-8.11.)
* Bugien metsästystä ja refaktorointia

### Viikko 46 (9.11.-15.11.)
* laitteen testaus oikeassa ympäristössä

### Viikko 47 (16.11.-22.11.)
* Valmis prototyyppi(?)

### Viikko 48 (23.11.-29.11.)
* Mahdollisten virheiden korjaamista

### Viikko 49 (30.11.-6.12.)
* Viimeistelyä ja viimeisten ongelmien korjaaminen

### Viikko 50 (7.12.-13.12.)
* Valmiin projektin esittely Haaga-Heliassa (keskiviikkona 9.12.?)


## Tekijät:

### Ilkka Jylhä
* Arduino ja Raspberry pi:llä ajettavan koodin kirjoittaminen ja suunnittelu.

### Antti Salo
* Käyttöliittymän suunnittelu ja koodaus. Kotelon suunnittelu ja 3D mallintaminen. 

### Sami Nisonen
* Dokumentointi ja avustavia tehtäviä suunnittelussa ja koodin kirjoittamisessa

