

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

