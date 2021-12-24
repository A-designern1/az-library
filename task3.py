

class Car:
    def __init__(self, color, year, type):
        self.color = color
        self.year = year
        self.type = type
    def Color(self, newcolor):
        self.color = newcolor
    def Type(self, newtype):
        self.type = newtype
    def Year(self, newyear):
        self.year = newyear
    def On(self):
        print('Автомобиль заведен')
    def Off(self):
        print('Автомобиль заглушен')

car = Car('blue', 3, 'lada')
car.On()
car.Off()
car.Year(10)




file = open('file.py')
file1 = open('file1.py', 'w')
for i in file:
    file1.write(i)




