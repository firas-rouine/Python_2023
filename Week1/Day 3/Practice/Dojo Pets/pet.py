from ninja import Ninja
class Pet:
    def __init__(self,name,type,triks,sound):
        self.name=name
        self.type=type
        self.tricks=triks
        self.health=100
        self.energy=100
        self.sound=sound
    def sleep(self):
        self.energy+=25
    def eat(self):
        self.energy+=5
        self.health+=10
    def play(self):
        self.health+=5
        return self
    def noise(self):
        print(f"the pet's sound is {self.sound}")
class Dog(Pet):
    def __init__(self,name,type,triks,sound):
        super().__init__(name,type,triks,sound)
        self.health+=10
        self.energy+=100
        
    def play(self):
        super().play()
        print(f"{self.name}: is play")
        return self
    def eat(self):
        super().eat()
        return self
    def noise(self):
        super().noise()
        return self
            
        
nibbles = Pet("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")
dog_1 = Dog("max","Berger allemand",'is invisible',"Hey Hey")
firas = Ninja("firas","rouine",nibbles,"Bacon",["pizza"])
firas.walk().walk().feed().bathe()
dog_1.play()


