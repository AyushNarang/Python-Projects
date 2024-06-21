def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Honda")
