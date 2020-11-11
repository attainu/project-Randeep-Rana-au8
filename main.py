class CarParking:
    def __init__(self, n):
        self.numberOfSlot = n
        self.slots = [0]*n

    def park(self, carNum, color):
        for i in range(len(self.slots)):
            if self.slots[i] == 0:
                self.slots[i] = carNum
                return("Car Parked at slot number", i+1)
   
        return "No parking available"
            
    def statue(self):
        print(self.slots)        



one = CarParking(5)
print(one.park("sfjsl", "white"))
one.statue()
print(one.park("sfjsl", "white"))
one.statue()
print(one.park("sfjsl", "white"))
one.statue()
print(one.park("sfjsl", "white"))
one.statue()
print(one.park("sfjsl", "white"))
one.statue()
print(one.park("sfjsl", "white"))
print(one.park("sfjsl", "white"))
print(one.park("sfjsl", "white"))
print(one.park("sfjsl", "white"))