class BNW:
    def max_speed(self):
        print("Max speed: 150 KM PER HOUR")
    def fuel_type(self):
        print("Fuel type:   Normal Gasoline")

class Ferrari:
    def max_speed(self):
        print("Max speed: 128 KM PER HOUR")
    def fuel_type(self):
        print("Fuel type: Premium Gasoline")
car_2 = BNW()
car_1 = Ferrari()

car_2.max_speed() 
car_2.fuel_type() 
car_1.max_speed() 
car_1.fuel_type() 