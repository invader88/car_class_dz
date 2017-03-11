class Carr:
    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price
    def __str__(self):
        return 'Model : {} \nColor : {} \nYear : {} \nPrice : {}'.format(self.model, self.color, self.year, self.price, sep="")

car1 = Carr('Audi', 'Red', 1999, '$12000')
print(car1)



class Showroom(Carr):
    def __init__(self, show_name, show_address):
        self.show_name = show_name
        self.show_address = show_address
        self.car_list = []

    def add_car(self,a_car):
        self.car_list.append(a_car)
    def show_all(self):
        for i in self.car_list:
            print('- - - -')
            print(i)
    def sell_car (self,sold_car):
        if sold_car in self.car_list:
            self.car_list.remove(sold_car)
            print("This car has been successfully sold")
        else:
            print("Such car not found")
            
        

