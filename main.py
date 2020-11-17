import sys
class CarParking:
    def __init__(self, n):
        self.numberOfSlot = n
        self.slots = [0]*n
        for i in range(n):
            self.slots[i] = {
                "slot": i+1,
                "status": "Available",
                "car_number" : None,
                "color": None,
            }
        print(f"Created a parking lot with {n} slots")

    def park(self, carNum, color):
        if (carNum == 0):
            return 0
        else:
            for i in range(len(self.slots)):
                if self.slots[i]["status"] == "Available":
                    self.slots[i] = {
                        "slot": i+1,
                        "car_number" : carNum,
                        "color": color,
                        "status": "Unavaiable"
                    }
                    return f"Allocated slot number: {i+1}"
        return "Sorry All slots are full, No parking available"

    def leave(self, slot_num):
        for i in range(len(self.slots)):
            if self.slots[i]["slot"] == int(slot_num):
                    self.slots[i] = {
                        "slot": i+1,
                        "car_number" : None,
                        "color": None,
                        "status": "Available"
                    }
                    return f"Slot number {i+1} is free"
        return "Car is not there"
            
    def status(self):
        print("Parking Details")
        for i in self.slots: 
            print(i)

    def find_car_slot_no(self, carNum):
        for i in range(len(self.slots)):
            if self.slots[i]["car_number"] == carNum:
                return f"{i+1}"
        return "Not Found"

    def registration_numbers_for_cars_with_colour(self, color):
        for i in self.slots:
            if i["color"] == color:
                print(i["car_number"])

    def slot_numbers_for_cars_with_colour(self, color):
        for i in self.slots:
            if i["color"] == color:
                print(i["slot"], end=",")
        print()
    

choice_input = input("if you want to run code from cmd type 1 and If you want to run code from file type 2 => ")
if choice_input == "1":
    first_input = input().split()
    # input2 = int(sys.argv[2])
    parking_lot = CarParking(int(first_input[1]))
    command_input = [""]
    while(command_input[0] != "exit"):
        print()
        command_input = input().split()
        
        if command_input[0] == "status":
            parking_lot.status()

        elif command_input[0] == "park":
            print(parking_lot.park(command_input[1], command_input[2]))

        elif command_input[0] == "leave":
            print(parking_lot.leave(command_input[1]))

        elif command_input[0] == "slot_number_for_registration_number":
            print(parking_lot.find_car_slot_no(command_input[1]))

        elif command_input[0] == "exit":
            print("Closing Parking lot")

        elif command_input[0] == "registration_numbers_for_cars_with_colour":
            parking_lot.registration_numbers_for_cars_with_colour(command_input[1])
        
        elif command_input[0] == "slot_numbers_for_cars_with_colour":
            parking_lot.slot_numbers_for_cars_with_colour(command_input[1])

        else:
            print("oops!! Invalid input try again")

elif choice_input == "2":
    with open("commands.txt", "r") as all_commands:
        for command in all_commands:
            new_command = command.split()
            if new_command[0] == "create_parking_lot" and len(new_command) == 2:
                parking_lot = CarParking(int(new_command[1]))


            if new_command[0] == "status":
                parking_lot.status()

            elif new_command[0] == "park":
                print(parking_lot.park(new_command[1], new_command[2]))

            elif new_command[0] == "leave":
                print(parking_lot.leave(new_command[1]))

            elif new_command[0] == "slot_number_for_registration_number":
                print(parking_lot.find_car_slot_no(new_command[1]))

            elif new_command[0] == "exit":
                print()

            elif new_command[0] == "registration_numbers_for_cars_with_colour":
                parking_lot.registration_numbers_for_cars_with_colour(new_command[1])
            
            elif new_command[0] == "slot_numbers_for_cars_with_colour":
                parking_lot.slot_numbers_for_cars_with_colour(new_command[1])

            elif "exit" in new_command and len(new_command) == 1:
                print("Closing parking lot")
                break

            else:
                print("oops!! Invalid input try again")

