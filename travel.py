class Travel:
    def __init__(self, ID, Destination, Flight, Price):
        self.ID = ID
        self.Destination = Destination
        self.Flight = Flight
        self.Price = Price
    def Reduce (self):
        if self.Price > 200:
            self.Price *= 0.9
    def Print (self):
        print("ID: ", self.ID)
        print("Destination: ", self.Destination)
        print("Flight: ", self.Flight)
        print("Price: ", self.Price)

toParis = Travel(23432, "Paris", "Sofia - Paris", 204.56)
toParis.Reduce()
toParis.Print()


