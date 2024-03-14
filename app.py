
# Interface:
class MusicalInstrument():
    def __init__(self, name):
        self.name = name
    def play(self):
        pass

# Instruments:
class Drum(MusicalInstrument):
    pass
class Tambourine(MusicalInstrument):
    pass
class Trombone(MusicalInstrument):
    pass
class Flute(MusicalInstrument):
    pass
class Organ(MusicalInstrument):
    pass
class Harmonica(MusicalInstrument):
    pass
class Bayan(MusicalInstrument):
    pass
class GrandPiano(MusicalInstrument):
    pass

# Types:
class Percussion(Drum, Tambourine):  
    def play(self):
        print(f"{self.name} Percussion plays")

class Wind(Trombone, Flute, Organ):   
    def play(self):
        print(f"{self.name} Wind plays")

class Keyboard(Harmonica, Bayan, GrandPiano):   
    def play(self):
        print(f"{self.name} Keyboard plays")
    

# Objects:
drum = Percussion("Drum")
tambourine = Percussion("Tambourine")
trombone = Wind("Trombone")
flute = Wind("Flute")
organ = Wind("Organ")
harmonica = Keyboard("Harmonica")
bayan = Keyboard("Bayan")
grand_piano = Keyboard("Grand Piano")

drum.play()
bayan.play()
