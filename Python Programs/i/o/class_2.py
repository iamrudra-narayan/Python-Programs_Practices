import numbers


class Calculator:
    def __init__(self,number):
        self.number = number

    def square(self):
        sq = self.number*self.number
        print(f"Square of the Number {self.number} is {sq}")

    def cube(self):
        cu = self.number*self.number*self.number
        print(f"Square of the Number {self.number} is {cu}")  

    def squareRoot(self):
        sqr = self.number**(0.5)
        print(f"Square of the Number {self.number} is {sqr}")      

calculate = Calculator(15)

n = int(input("Enter A Number: "))

calculate.number = 16

calculate.square()
calculate.cube()
calculate.squareRoot()