# class Type():
#     def play(self):
#         pass

# class MusicalInstrument():
#     def __init__(self, type: Type):
#         self.type = type

#     def play(self):
#         self.type.play()


# class Percussion(Type):
#     def __init__(self, name):
#         self.name = name
    
#     def play(self):
#         print(f"{self.name} Percussion plays")

# class Wind(Type):
#     def __init__(self, name):
#         self.name = name
    
#     def play(self):
#         print(f"{self.name} Wind plays")

# class Keyboard(Type):
#     def __init__(self, name):
#         self.name = name
    
#     def play(self):
#         print(f"{self.name} Keyboard plays")
    

# drum = MusicalInstrument(Percussion("Drum"))
# tambourine = MusicalInstrument(Percussion("Tambourine"))
# trombone = MusicalInstrument(Wind("Trombone"))
# flute = MusicalInstrument(Wind("Flute"))
# organ = MusicalInstrument(Wind("Organ"))
# harmonica = MusicalInstrument(Keyboard("Harmonica"))
# bayan = MusicalInstrument(Keyboard("Bayan"))
# grand_piano = MusicalInstrument(Keyboard("Grand Piano"))

# flute.play()










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
