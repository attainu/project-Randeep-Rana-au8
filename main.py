class CarParking:
    def __init__(self, n):
        self.numberOfSlot = n
        self.slots = [0]*n

    def park(self, carNum, color):
        if (carNum == 0):
            return 0
        else:
            for i in range(len(self.slots)):
                if self.slots[i] == 0:
                    self.slots[i] = {
                        "slot": i+1,
                        "car_number" : carNum,
                        "color": color
                    }
                    return f"{carNum} Parked at slot number {i+1}"
   
        return "No parking available"

    def leave(self,car_number):
        for i in range(len(self.slots)):
            if self.slots[i]["car_number"] == car_number:
                    self.slots[i] = 0
                    return f"{car_number} has leaved"
        return "Car is not there"
            
    def status(self):
        print("Parking Details")
        for i in self.slots: 
            print(i)

    # def car

input1 = input()
input2 = int(input())
input1 = CarParking(input2)

for i in range(input2):
    new_input1 = input("Enter car num: ")
    new_input2 = input("Enter car color: ")
    if new_input1 == "":
        print(input1.park(0, 0))
    else:
        print(input1.park(new_input1, new_input2))

print(input1.park("uk08-1192", "white"))
print(input1.leave("UP58-3929"))
print(input1.leave("uk08-1192"))
print()
print()

input1.status()
input1.status()

input3 = ""
while(input3 != "exit"):
    input3 = input()
    if input3 == "status":
        input1.status()
    elif input3[0:4] == "park":
        print("Parks")
        