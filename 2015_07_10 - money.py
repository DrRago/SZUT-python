import time

class Money(object):

    __exchange_rate = {"USD": 0.899847,
                       "GBP": 1.37377,
                       "EUR": 1.0,
                       "JPY": 0.00716}

    def __init__(self, value=0, currency="EUR"):
        if currency in self.__exchange_rate:
            self.__currency = currency
        else:
            raise KeyError("currency (%s) existiert nicht!" % currency)
        try:
            self.__value = float(value)
            self.__value = round(self.__value, 2)
        except:
            raise TypeError("value muss vom Typ float sein!")

    def getValue(self):
        """
        value des Geldes zurueckgeben.
        Eingabewert: Keiner
        Rueckgabewert: value als float, gerundet auf 2 Stellen
        """
        return self.__value

    def getCurrency(self):
        """
        currency des Geldes zurueckgeben.
        Eingabewert: Keiner
        Rueckgabewert: currency des Geldobjektes
        """
        return self.__currency

    def setValue(self, value):
        self.__value = float(value)
        self.__value = round(self.__value, 2)

    def setCurrency(self, currency):
        if currency in self.__exchange_rate:
            self.__currency = currency
        else:
            raise KeyError("currency (%s) existiert nicht!" % currency)

    def getEuro(self):
        """
        Geldobjekt in Euro umformen.
        Eingabewert: Keiner
        Rueckgabewert: Geldobjekt in Euro umgewandelt
        """
        val = round(self.__value * self.__exchange_rate[self.__currency], 2)
        return Money(val, 'EUR')

    def add(self, val1):
        """
        Geld addieren.
        Eingabewert: Das zu addierende Geld
        Rueckgabewert: Neuer Geldstand
        """
        temp_money = self.getEuro().getValue() + val1.getEuro().getValue()
        new_money = Money(temp_money/self.__exchange_rate[self.getCurrency()], self.getCurrency())
        return new_money

    def __add__(self, other):
        return self.getEuro().getValue() + other.getValue(), self.getEuro().getCurrency()

    def __sub__(self, other):
        return self.getEuro().getValue() - other.getValue(), self.getEuro().getCurrency()

    def __iadd__(self, other):
        return self.getEuro().getValue() + other.getValue(), self.getEuro().getCurrency()

    def __isub__(self, other):
        return self.getEuro().getValue() - other.getValue(), self.getEuro().getCurrency()

    def __eq__(self, other):
        return self.getEuro().getValue() == other.getValue()

    def __gt__(self, other):
        return self.getEuro().getValue() > other.getValue()

    def __ge__(self, other):
        return self.getEuro().getValue() >= other.getValue()

    def __lt__(self, other):
        return self.getEuro().getValue() < other.getValue()

    def __le__(self, other):
        return self.getEuro().getValue() <= other.getValue()

    def __neg__(self):
        if self.getValue() < 0:
            return self.getValue()
        else:
            return self.getValue() * -1

    def __ne__(self, other):
        return self.getEuro().getValue() != other.getValue()

class Konto(Money):
    def __init__(self, currency, inhaber):
        Money.__init__(self, currency, 0)
        self.__inhaber = inhaber
        self.__kontoauszug = [str(self)]

    def einzahlen(self, currency, value):
        einzahlung = Money(currency, value)
        self.value = (self + einzahlung).value
        eintrag = time.asctime() + " " + str(einzahlung) + " neuer Kontostand: " + self.currency + " " + format(self.value, ".2f")
        self.__kontoauszug += [eintrag]
        
    def auszahlen(self, currency, value):
        self.einzahlen(currency, -value)
        
    def druckeKontoauszug(self):
        for i in self.__kontoauszug:
            print(i)
            self.__kontoauszug = [str(self)]
            
    def __str__(self):
        return "Konto von " + self.__inhaber + ":\nKontostand am " + time.asctime() + ": " + format(self.value, ".2f") + " " + self.currency

if __name__ == "__main__":
    konto = Konto("EUR", "Leonhard")
    konto.einzahlen(42, "EUR")
