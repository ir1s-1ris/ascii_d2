class Car:
    def __init__(self):
        print('двигатель заведён')
        self.name = 'corolla'
        self.__make = 'toyota'
        self._model = 1999

car_a = Car()
print(car_a.model)