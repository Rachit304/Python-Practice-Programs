class Vehicle:
    Petrol_rate = 98.04

    def __init__(self):
        self.v_type = input("Enter Ur Vehicle Type : ")
        self.brand = input("Enter Ur Vehicle Brand : ")
        self.model = input("Enter Ur Vehicle Model: ")
        self.t_size = int(input("Enter the size of Fuel tank: "))
        self.f_level = int(input("Enter Ur Current fuel level : "))

    def full_tank(self):
        amount = self.t_size - self.f_level
        new_level = self.t_size
        print("Fuel: ", new_level, end=" ")
        print("\tCharge: %.2f" % (amount * self.Petrol_rate))

        print("........TANK FULL.......")
        self.f_level = self.t_size

    def update_fuel_tank(self):
        if self.f_level <= 3:
            print("LOW-FUEL WARNING : Immediate need to Fill Fuel... ")
        elif self.f_level == self.t_size:
            print("TANK IS FULL..no need to worry")
        elif self.f_level > self.t_size:
            print("Invalid Number !!")
        else:
            print("Sufficient Fuel : Ur Fuel is", self.f_level, " ltrs..Ur call to fill it or not")

    def get_fuel(self):
        amount = int(input("How many litters You want to add : "))
        self.f_level = self.f_level + amount
        new_level = self.f_level
        if new_level < self.t_size:
            print("Fuel: ", new_level, end=" ")
            print("\tCharge: %.2f" %(amount*self.Petrol_rate))
        else:
            print("Fuel Overloaded")

    def drive(self):
        print("Wow....I'm driving ", self.model)


print("--------------Enter to the World of Automobiles--------------\n")


for i in range(2):
    obj = Vehicle()

    obj.update_fuel_tank()

    ans = input("Do You want to fill full tank(y/n) : ")
    if ans == 'y':
        obj.full_tank()
    elif ans == 'n':
        obj.get_fuel()
    else:
        print("Invalid Input")

    obj.update_fuel_tank()
    obj.drive()
    print("---------------------------------------------------------\n")
