class Vehicle:
    def __init__ (self, name, maxSpeed, mileage, capacity):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage
        self.capacity = capacity
    def Print (self):
        print("Vehicle Name: " , self.name)
        print("Speed: ", self.maxSpeed)
        print("Mileage: ", self.mileage)
        print("Capacity: ", self.capacity)
vehicleBus = Vehicle("Volvo", 200, 14, 50)
vehicleBus.Print() 