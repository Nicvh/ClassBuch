import math

class Buch:
    def __init__(self, titel, autor, seitenanzahl):
        self.titel = titel
        self.autor = autor
        self.seitenanzahl = seitenanzahl
        self.seiten_gelesen = 0
        self.abschluss_tage = None  # Speichert die geschätzten Tage

    def info(self):
        print(f"'{self.titel}' von {self.autor}, {self.seitenanzahl} Seiten.")

    def lesezeit_schaetzen(self, minuten_pro_seite=5, lesedauer_pro_tag_minuten=240):
        gesamtzeit_minuten = self.seitenanzahl * minuten_pro_seite
        tage = math.ceil(gesamtzeit_minuten / lesedauer_pro_tag_minuten)  # Aufrunden
        self.abschluss_tage = tage  # Speichern, damit wir sie später verwenden können
        print(f"Geschätzte Gesamtlesezeit: {gesamtzeit_minuten} Minuten.")
        print(f"Bei {lesedauer_pro_tag_minuten} Minuten Lesen pro Tag brauchst du ungefähr {tage} Tage.")
        return tage

    def lesen(self, seiten):
        if seiten <= 0:
            print("Bitte eine positive Seitenzahl angeben.")
            return
        verbleibende_seiten = self.seitenanzahl - self.seiten_gelesen
        if seiten >= verbleibende_seiten:
            self.seiten_gelesen = self.seitenanzahl
            print(f"Du hast die letzten {verbleibende_seiten} Seiten gelesen. Buch abgeschlossen!")
            if self.abschluss_tage:
                print(f"✅ Du hast das Buch in {self.abschluss_tage} Tagen abgeschlossen!")
            else:
                print("✅ Buch abgeschlossen!")
        else:
            self.seiten_gelesen += seiten
            print(f"Du hast {seiten} Seiten gelesen. Insgesamt {self.seiten_gelesen}/{self.seitenanzahl} Seiten gelesen.")

# Beispiel-Nutzung:
mein_buch = Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", 320)

mein_buch.info()
mein_buch.lesezeit_schaetzen()  # berechnet und speichert die 7 Tage
mein_buch.lesen(50)
mein_buch.lesen(270)  # beendet das Buch