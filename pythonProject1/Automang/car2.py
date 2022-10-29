import random

class Car:
    def __init__(self, model):
        self.model = model
        self.speed = random.randint(1, 5)

    def get_model(self):
        return self.model

car1 = Car("BMW")
car2 = Car("Audi")

print(car1.get_model(), car1.speed)
print(car2.get_model(), car2.speed)