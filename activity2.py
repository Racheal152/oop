class Dog:
    def move(self):
        return "Running 🐕"

class Bird:
    def move(self):
        return "Flying 🕊️"

class Fish:
    def move(self):
        return "Swimming 🐟"

animals = [Dog(), Bird(), Fish()]
for animal in animals:
    print(animal.move())