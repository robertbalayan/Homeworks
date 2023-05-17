#PEN VOSHUM EN KAPIKIEN ZIBILNA VOBSHUM
from math import pi

class Animal:
    def __init__(self,sound,type):
        self.sound = sound
        self.type = type
        print(sound)
        print(type)
class monkey(Animal):
    def fact(self):
        return "Im monkey"

Ararmbutan = monkey(sound="GUGUUGUGUG",type="Arambutan")
Ararmbutan.fact()

