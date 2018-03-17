# Contents

- Durchschnittsrechner
- Befreundete und vollkommene Zahlen
- Sexteten
- Verschlüsselungsaufgabe

# Durchschnittsrechner

Entwickeln Sie ein Programm zur Berechnung von Mittelwerten (Durchschnitt) für beliebig viele positive Zahlen (Kommazahlen, einschließlich Null). Erweitern Sie das Programm um eine Diagrammdarstellung der eingegebenen Werte (siehe Beispiel, Kommazahlen sollen gerundet werden). Verwenden Sie nur einfache Variablen (keine Listen), Schleifen, Ein- und Ausgabefunktionen, Umwandlungsfunktionen für Text in Zahlen, round(…) und grundlegende Rechenoperationen für die Realisierung.

Beispielhafter Programmdurchlauf:

Bitte Wert eingeben (&lt;0 beendet): 3.3
Bitte Wert eingeben (&lt;0 beendet): 3.8
Bitte Wert eingeben (&lt;0 beendet): 4.2
Bitte Wert eingeben (&lt;0 beendet): 4.7
Bitte Wert eingeben (&lt;0 beendet): -1

Diagramm:
###
####
####
#####

Durchschnitt: 4.0

Alternativ kann das Programm auch zu Beginn die beabsichtige Anzahl der Eingaben erfragen.

Testen und dokumentieren Sie Ihr Programm hinreichend und erstellen Sie ein entsprechendes Protokoll nach den bekannten Vorgaben.

Hinweis: Die Funktion float(…) kann verwendet werden, um einen Text in eine Kommazahl umzuwandeln. Die Funktion round(…) rundet eine Kommazahl.

**Abgabe** online: **Protokoll als PDF** Dokument ( **ebenfalls gedruckt** abzugeben) und den **Quelltext als .py** Datei (ggf. in einem ZIP Archiv).


# Befreundete und vollkommene Zahlen
In der Mathematik werden natürliche Zahlen als vollkommen bezeichnet, wenn die Summe ihrer echten Teiler der Zahl entspricht. Die Zahl 6 hat die Teiler 1, 2 und 3. Da die Summer aus diesen Zahlen 6 ergibt, ist die 6 eine vollkommene Zahl.

Zwei unterschiedliche natürliche Zahlen heißen befreundet, wenn die Summe der Teiler der einen Zahl der anderen entspricht und umgekehrt. Beispielsweise sind die Zahlen 220 und 284 befreundet, denn die Summer der Teiler von 220 ist 284 und die Summe der Teiler von 284 ist 220:

| Zahl | Teiler | Summe der Teiler |
| --- | --- | --- |
| 220 | 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 | 284 |
| 284 | 1, 2, 4, 71, 142 | 220 |

Weitere Informationen zu  [befreundeten](https://de.wikipedia.org/wiki/Befreundete_Zahlen) und  [vollkommenen Zahlen](https://de.wikipedia.org/wiki/Vollkommene_Zahl) finden Sie auf den entsprechenden Seiten der  [Wikipedia](https://de.wikipedia.org/).

## Aufgabe
Entwickeln Sie ein Programm, dass bis zu einem vom Nutzer eingegebenen Wert alle befreundeten und vollkommenen Zahlen ausgibt.

Beispiel:

Teiler - Test  
  
Geben Sie einen Endwert an: 100000  
6 ist vollkommen  
28 ist vollkommen  
220 und 284 sind befreundet  
284 und 220 sind befreundet  
496 ist vollkommen  
1184 und 1210 sind befreundet  
1210 und 1184 sind befreundet  
2620 und 2924 sind befreundet  
2924 und 2620 sind befreundet  
5020 und 5564 sind befreundet  
5564 und 5020 sind befreundet  
6232 und 6368 sind befreundet  
6368 und 6232 sind befreundet  
8128 ist vollkommen  
10744 und 10856 sind befreundet  
10856 und 10744 sind befreundet   
12285 und 14595 sind befreundet  
14595 und 12285 sind befreundet  
17296 und 18416 sind befreundet  
18416 und 17296 sind befreundet  
63020 und 76084 sind befreundet  
66928 und 66992 sind befreundet  
66992 und 66928 sind befreundet  
67095 und 71145 sind befreundet  
69615 und 87633 sind befreundet  
71145 und 67095 sind befreundet  
76084 und 63020 sind befreundet  
79750 und 88730 sind befreundet  
87633 und 69615 sind befreundet  
88730 und 79750 sind befreundet  
fertig!  

Erweitern Sie Ihr Programm dann so, dass doppelte Ausgaben für befreundete Zahlen unterdrückt werden.

Beispiel:  

Teiler - Test  
  
Geben Sie einen Endwert an: 100000  
6 ist vollkommen  
28 ist vollkommen  
220 und 284 sind befreundet  
496 ist vollkommen  
1184 und 1210 sind befreundet  
2620 und 2924 sind befreundet  
5020 und 5564 sind befreundet  
6232 und 6368 sind befreundet  
8128 ist vollkommen  
10744 und 10856 sind befreundet  
12285 und 14595 sind befreundet  
17296 und 18416 sind befreundet  
63020 und 76084 sind befreundet  
66928 und 66992 sind befreundet  
67095 und 71145 sind befreundet  
69615 und 87633 sind befreundet  
79750 und 88730 sind befreundet  
fertig!  

Das Programm soll neben eventuell weiteren Funktionen mindestens die folgenden Funktionen enthalten und verwenden:

- Eine Funktion, die zu einer natürlichen Zahl eine Liste aller Teiler außer ihr selbst zurückliefert.
- Eine Funktion, die zu einer natürlichen Zahl die befreundete Zahl zurückliefert, wenn diese existiert. Fall es keine befreundetete Zahl gibt, soll sie None zurückliefern.

Kommentieren und testen Sie Ihr Programm hinreichend und fertigen Sie eine Dokumentation in Form eines Protokolls nach den bekannten Vorgaben an.




# Sexteten
Im Land der Sexteten haben die Bewohner an jeder Hand drei Greifer. Ihr Zahlensystem ist ein Stellenwertsystem wie unser Dezimalsystem, verfügt aber dementsprechend nur über 6 Zeichen, die folgende Werte haben:

**Zeichen-Wert**

**&lt; 0**

**&gt; 1**

**\* 2**

**+ 3**

**( 4**

**) 5**

Wenn eine Sextetenzahl aus mehreren Zeichen besteht, so sind die Stellen wie in unserem Dezimalsystem angeordnet, d.h. die höchstwertige Stelle ganz links und die niedrigstwertige ganz rechts.

Schreiben Sie ein Programm, das die Rechenaufgabe im Sexteten System einliest und eine entsprechende Lösungsdateil erzeugt. Orientieren Sie sich dabei an den Musterdateien. Leerzeichen sind keine gültigen Eingabezeichen.

Zerlegen Sie das Problem in Teilprobleme. Es empfiehlt sich, zunächst (Unter-)Programme zu einzelnen Teilproblemen zu schreiben und zu testen.

_Hinweise_

Die Zeichen für die Darstellung einer nicht negativen ganzen Zahl im Sexteten-System lassen sich als Reste bei fortgesetzter ganzzahliger Division durch 6 ermitteln.

Für die Zahl 125 ergibt sich die Darstellung +\*) wie folgt:

125 / 6 = 20 Rest 5 niedrigstwertige Sexteten-Ziffer: )

20  / 6 = 3 Rest 2 nächst höherwertige Ziffer: \*

3   / 6 = 0 Rest 3 nächst höherwertige Ziffer: +

Da der Quotient 0 geworden ist, ist die Konvertierung beendet. Eine Fortführung des Verfahrens würde nur noch führende &lt;-Zeichen ermitteln.

Um umgekehrt den Wert einer Zahl aus ihrer Darstellung im Sexteten-System abzuleiten, geht man die Zeichen von links nach rechts durch. Zu Beginn wird der Wert der Zahl mit 0 initialisiert. Für jedes Zeichen wird der alte Zahlenwert mit 6 multipliziert und dann der Wert des jeweiligen Zeichens addiert. Für die Darstellung +\*) ergibt sich:

Zahl ist 0

+ entspricht 3 Zahl wird 0 \* 6 + 3 = 3

\* entspricht 2 Zahl wird 3 \* 6 + 2 = 20

) entspricht 5 Zahl wird 20\* 6 + 5 = 125

Ein anderes Verfahren besteht darin jedes Zeichen mit seiner entsprechenden Wertigkeit zu multiplizieren und dann aus den Zahlen die Summe zu bilden.

+ entspricht 3: Zahl wird 3 \* 62 = 108

\* entspricht 2: Zahl wird 2 \* 61 = 12

) entspricht 5: Zahl wird 5 \* 60 = 5

Summe: 125


Das Programm soll neben eventuell weiteren Funktionen mindestens die folgenden Funktionen enthalten und verwenden:

- Eine Funktion, die eine natürliche Zahl in eine Sextetenzahl wandelt.
- Eine Funktion, die eine Sextetenzahl in eine natürliche Zahl wandelt.

_Teil 2 der Aufgabe_

Das Programm soll in der Lage sein eine Sexteten-Aufgabendatei einzulesen. Eine Beispieldatei wird zur Verfügung gestellt. Die darin enthaltene Aufgabe soll durch ihr Programm gelöst werden. Die Ergebnisse sollen im Anschluss in einer Lösungsdatei gespeichert werden. Eine solche Datei wird ebenfalls zu Verfügung gestellt.

Bitte wählen Sie für das Format der Aussgabedatei GENAU das Format der Beispieldatei. Die Ausgabedatei wird mittels automatischem Test überprüft. Jede Veränderung des Ausgabeformats wird als Fehler registriert. Beachten Sie also bitte die Größe der Datei,  die Anzahl der Zeilenumbrüche, die Leerzeichen, Einrückungen usw.

Kommentieren und testen Sie Ihr Programm hinreichend und fertigen Sie eine Dokumentation in Form eines Protokolls nach den bekannten Vorgaben an.



# Verschlüsselungsaufgabe

**Einführung**

Was ist &quot;Verschlüsselung&quot;? Ein einfaches Beispiel ist ein Dokument in einem verschlossenen Raum. Nach Möglichkeit haben nur Menschen einen Schlüssel dazu, die berechtigt sind, das Dokument zur Kenntnis zu nehmen. Möchte man das Dokument verschicken, so ist es nach allgemeiner Auffassung zu aufwändig den Raum mitzuschicken. Also &quot;verschlüsselt&quot; man den Text, indem man ihn unleserlich macht. Nur wer im Besitz einer geheimen Information ist (einem &quot;Schlüssel&quot;), der kann den Text lesen.

Wir werden uns hier mit einem der einfachsten Verschlüsselungsverfahren beschäftigen, der Substitution. Nach einem bestimmten Verfahren werden die Buchstaben eines Textes durch Symbole oder (vorzugsweise) andere Buchstaben ersetzt.

Monoalphabetisch heißt die Substitution, wenn jeder Buchstabe durch das gleiche Symbol ersetzt wird. Maria Stuart, einst schottische Königin, verlor bei der Bestätigung des Babington-Komplotts durch einen monoalphabetisch verschlüsselten Texts aus den Kerkern Königin Elisabeths 1587 den Kopf. Es war nämlich nicht allzu schwer ihn zu entschlüsseln.

Wir wollen unseren Kopf behalten und verschlüsseln daher polyalphabetisch. Es oll nicjht verschwiegen werden, dass es den Deutschen mit der polyalphabetisch verschlüsselnden Maschine ENIGMA nicht viel besser erging, nachdem Alan Turing sie mit seiner &quot;Bombe&quot; knackte.

**Verschlüsselung Einstieg:**

Es ist eine Funktionen zu erstellen:

def encodeWithCesar(sourcefile, destfile, caesarPass)

Aufgabe der Funktion ist es die Datei sourcefile nach dem Additionsverfahren zu verschlüsseln indem der Original Text durch einen verschlüsselten substituiert wird. Der Parameter caesarPass:String stellt dabei den Schlüssel dar. Der verschlüsselte Text soll in destfile abgespeichert werden.

Ein Zeichen repräsentiert natürlich nur ein Zeichen bei einer entsprechenden Kodierung. Addiert man nun &#39;1&#39; + &#39;2&#39;, so ergibt dies nicht etwa &#39;3&#39;, sondern &#39;c&#39;. Das ist nicht weiter erstaunlich, wenn man z.B. den ASCII-Code betrachtet:

&#39;1&#39; -&gt; 49

&#39;2&#39; -&gt; 50

&#39;c&#39; -&gt; 99

Es soll zu dem ersten Zeichen von sourcefile der erste Wert des von caesarPass addiert werden. Danach weiter mit dem zweiten Zeichen von sourcefile und caesarPass, dem Dritten und dem Vierten. Meist ist das Passwort kürzer als die Quelldatei. Dann fängt man nach dem letzten Zeichen von caesarPass wieder bei dem ersten Zeichen von caesarPass an. Ein Beispiel dazu:

Quelldatei:  H A L L O W E L T Der Text ist länger als der Schlüssel:

caesarPass: I C H

Schlüsel:   I C H I C H I C H Der Schlüssel wird wiederholt verwendet.

Ergebnis:   æ ä ö ò Æ ƒ  Ä   Å   £Die Summe der Zeichen

Es ist also &#39;H&#39; + &#39;I&#39; = &#39;æ&#39;, wenn man z.B. die cp850 zu Grunde legt.

**Entschlüsselung:**

Es ist eine Funktion zu erstellen, die folgenden Prototyp hat:

def decodeWithCesar(sourcefile, destfile, ceaesarPass)

**Verschlüsselung Fortsetzung**

Die Verschlüsselung soll noch sicherer werden. Dazu wollen wir zu jedem Zeichen noch eine (fast) zufällige Zahl addieren. Hierfür nutzen wir das random Modul. Das random Modul erzeugt „zufällige&quot; Zahlen. Diese sind allerdings nicht wirklich zufällig, sondern lediglich zufällig verteilte Werte, die mittels einer mathematischer Funktion intern berechnet werden. Starten sie den Zufallszahlengenerator mehrfach mit dem gleichen Startwert, so erhalten Sie auch immer die gleich Abfolge von quasi zufälligen Zahlen. Normalerweise nutzt das random Modul bei der Initiierung die aktuelle Systemzeit des Rechners, die bei dem Start des Programms natürlich immer eine andere ist. Wir wollen den Startwert des Zufallszahlengenerators mittels der random.seed() Funktion für unsere Bedürfnisse beeinflussen. Dazu bilden wir den absoluten Wert CRC32-Checksumme (_cyclic redundancy check_ ) des Passwortes Checksummenbildung mit abs(zlib.crc32(password)). Die CRC32 Funktion erwartet als Datentyp bytes. Deswegen muss das Passwort von String in bytes umgewandelt werden. Wir werden dazu die Zeichencodierung UTF-8 verwenden. Das Ergebnis der Prüfsummenbildung ist eine positive 32-Bit Zahl. Diese teilen wir in vier 8-Bit Ganzzahlen auf. Die Zahlen 0-2 (die unteren drei) stellen den Startwert des Zufallsgenerators dar (Zahlenwerte von 0 – 16777215). Die obere Zahl (Zahl 3) wird genutzt um jeden Buchstaben des Originaltextes damit zu verschieben. Genutzt werden also mehrere Schritte zum Ver- und Entschlüsseln:

1) CRC32 Prüfsumme des Passwortes bilden → 32-Bit Zahlencode

2) Prüfsumme zerlegen → vier 8-Bit Zahlen (Z3-Z0) → Z3 Z2 Z1 Z0 (big Endian)

3) Z2-Z0 verwenden für die Initialisierung des Zufallszahlengenerators

4) Schleife

  4a) Originalzeichen um Z3 verschieben

  4b) Zufallszahl im Bereich 0-255 addieren

  4c) Passwortzeichen addieren

  4d) Wert % 256 berechnen

**Zum Dateiformat**

Um unsere eigenen verschlüsselten Dateien besser nutzen zu können sollen einige Vereinbarungen getroffen werden. Wir übernehmen standardmäßig den Dateinamen der Originaldatei. Die Dateiendung unserer verschlüsselten Dateien ist standardmäßig „cip&quot;. Der Dateianfang unserer „cip-Dateien&quot; ist wie folgt aufgebaut:

Zeichen 1-3: c i p  also als Binärzahlen 99 151 112

Zeichen 4: eine Zahl von 1-255 (Länge der folgenden Dateiendung)

Zeichen 5 – x: Die Dateiendung der Originaldatei

Beispiel für eine verschlüsselte Bitmap-Datei: Beispiel.bmp → Beispiel.cip

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| &#39;c&#39; | &#39;i&#39; | &#39;p&#39; | 3 | &#39;b&#39; | &#39;m&#39; | &#39;p&#39; | ... |   |   |

Alle von den Gruppen verschlüsselten Dateien müssen vollständig kompatibel sein. Entschlüsseln sie zum Testen also auch Dateien anderer Gruppen. Es muss die Originaldatei wieder entstehen.

**Zu den Komandozeilen-Parametern:**

Der Aufruf des Programms erfolgt mit mehreren Argumenten:
-c / --cipher -&gt; cipher (verschlüsseln)
-d / --decipher -&gt; decipher (entschluesseln)
-p / --password &lt;password&gt; (Passwort für die Verschlüsselung)
-i / --inputfile &lt;inputfile&gt;
-o / --outputfile &lt;outputfile&gt;


Das bedeutet das Programm benötigt mindestens 3 evtl. 4 Parameter.

Bsp:

Verschlüsseln :                 python mycipher.py -c -p geheim -i MeinText.txt

Entschlüsseln der entstandenen Datei: python mycipher.py -d -p geheim -i MeinText.cip

Verschlüsseln mit Angabe des Ziels:   python mycipher.py -c -p auchgeheim -i MeinBild.txt -o Ciphered.cry

Nutzen Sie für die Kommandozeilen-Paramter das argparse-Module.

**ACHTUNG: Ihre &quot;\*.cip&quot; Dateien müssen miteinander kompatibel sein.**