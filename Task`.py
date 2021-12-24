# # class Mebel:
# #    pass
# # mebel1 = Mebel()
# # mebel1.tovar = 'divan'
# # mebel1.price = 10000
# # mebel1.valuta = 'rub'
# # mebel1.ves = 100
# # mebel1.edinitsi = 'kg'
# # mebel2 = Mebel()
# # mebel2.tovar = 'kreslo'
# # mebel2.price = 7000
# # mebel2.valuta = 'rub'
# # mebel2.ves = 50
# # mebel2.edinitsi = 'kg'
# # def furniture(mebel):
# #     print(f'Tovar: {mebel.tovar}, Price: {mebel.price} {mebel.valuta}, Ves: {mebel.ves} {mebel.edinitsi}')
#
# # furniture(mebel1)
# # furniture(mebel2)
#
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def printInfo(self):
#         print(f'{self.name} is eating')
#
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#     def dog(self):
#         print(f'Dog is barking. breed: {self.breed}')
#
#
# class Cat(Animal):
#     def cat(self):
#         print(f'Meow.')
#
#
# class Frog(Animal):
#     def printInfo(self):
#         print(f'Frog is eating')
#
#
# frog1 = Frog('Kisa')
# frog1.printInfo()




#
# class Student:
#     def __init__(self, name='Ivan', age='18', groupNumber='10A'):
#         self.name = name
#         self.age = age
#         self.groupNumber = groupNumber
#
#     def getName(self):
#         print(f'name: {self.name}')
#     def GetGroupName(self):
#         print(f'groupNumber: {self.groupNumber}')
#     def getAge(self):
#         print(f'age: {self.age}')
#     def setNameAge(self, newname, age):
#         self.name = newname
#         self.age = age
#     def setGroupNumber(self, groupNumber):
#         self.groupNumber = groupNumber
#
# student1 = Student()
# student1.setNameAge('Azat', 10, '10b')
#
# student2 = Student()
# student2.setNameAge('Azamat', 16, '10A')
#
# student3 = Student()
# student3.setNameAge('Aynur', 31, '1a')
#
# student4 = Student()
# student4.setNameAge('Kirill', 12, '2c')
#
# student5 = Student()
# student5.setNameAge('Max', 20, '3d')



#
# class Math:
#
#     def addition(self, a, b):
#         print(a + b)
#     def multiplication(self, a, b):
#         print(a*b)
#     def division(self, a, b):
#         print(a / b)
#     def subtraction(self, a, b):
#         print(a - b)
#
# num1 = Math()
# num1.subtraction(5, 3)
#
#





# class Car:
#     def __init__(self, color, year, type):
#         self.color = color
#         self.year = year
#         self.type = type
#     def Color(self, newcolor):
#         self.color = newcolor
#     def Type(self, newtype):
#         self.type = newtype
#     def Year(self, newyear):
#         self.year = newyear
#     def On(self):
#         print('Автомобиль заведен')
#     def Off(self):
#         print('Автомобиль заглушен')
#
# car = Car('blue', 3, 'lada')
# car.On()
# car.Off()
# car.Year(10)


#
#
# class Soda:
#     def __init__(self, dobavka=''):
#         self.dobavka = dobavka
#
#     def Show_my_drink(self):
#         if self.dobavka != '':
#             print(f'Газировка и {self.dobavka}')
#         else:
#             print('Обычная газировка')
#
# soda1 = Soda('limon')
# soda1.Show_my_drink()






class Soda:
    def __init__(self, dobavka=''):
        self.dobavka = dobavka

    def Show_my_drink(self):
        if self.dobavka != '':
            print(f'Газировка и {self.dobavka}')
        else:
            print('Обычная газировка')

soda1 = Soda('limon')
soda1.Show_my_drink()

























