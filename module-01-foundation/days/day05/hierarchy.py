class Animal:
    def init(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")
    
    def move(self):
        print(f"{self.name} moves")

class Dog(Animal):
    def speak(self):  # Override the speak method
        print(f"{self.name} barks: Woof!")
    
    def move(self):
        print(f"{self.name} runs")
    
    def speak_loudly(self):
        # Call the parent's version too
        super().speak()  # Uses Animal's speak
        self.speak()     # Uses Dog's speak

class Cat(Animal):
    def speak(self):  # Override differently
        print(f"{self.name} meows: Meow!")
    
    def move(self):
        super().move()  # Call parent, then add
        print(f"{self.name} sneaks quietly")

# Test
animals = [
    Animal("Generic"),
    Dog("Rex"),
    Cat("Whiskers")
]

for animal in animals:
    animal.speak()  # Each speaks differently!

# Output:
# Generic makes a sound
# Rex barks: Woof!
# Whiskers meows: Meow!