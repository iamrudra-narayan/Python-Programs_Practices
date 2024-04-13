import random

seat = [1,2,3,4,5,6,7,8,9,10]
print(seat)

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
            seat.remove(len(seat))
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        if seatNo in seat:
            print("Type a Valid Seat No.")
        else:    
            seat.append(seatNo)

intercity = Train("Intercity Express: 14015", 90, len(seat))
intercity.getStatus() 
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket(5)
print(seat)


    