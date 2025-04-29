# Zoo-Verwaltungssystem

# Klasse Art
class Art:
    def __init__(self, name):
        self.name = name

# Oberklasse Tier
class Tier:
    def __init__(self, name, art_name):
        self.name = name
        self.art = Art(art_name)

# Unterklasse Hund
class Hund(Tier):
    def __init__(self, name):
        super().__init__(name, "Hund")

# Pfleger-Klasse
class Pfleger:
    def __init__(self, name):
        self.name = name
        self.tiere = []

    def tier_hinzufuegen(self, tier):
        self.tiere.append(tier)

# Fuetterung-Klasse
class Fuetterung:
    def __init__(self, pfleger, tier):
        self.pfleger = pfleger
        self.tier = tier

    def starten(self):
        print(f"Pfleger {self.pfleger.name} füttert das Tier {self.tier.name} (Art: {self.tier.art.name}).")

# ---------------------------
# Beispiel-Nutzung
# ---------------------------

# Hund erstellen
bella = Hund("Bella")

# Pfleger erstellen
pfleger = Pfleger("Tom")
pfleger.tier_hinzufuegen(bella)

# Fütterung starten
runde = Fuetterung(pfleger, bella)
runde.starten()