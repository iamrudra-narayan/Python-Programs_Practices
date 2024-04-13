class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,product):
        self.name = name
        self.salary = salary
        self.product = product  

    def getDetails(self):
        print(f"The Employee {self.name} work in {self.company}.\nHis Product is {self.product} and Salary is {self.salary}.")

employee_1= Programmer("Rudra",100,"Github")
employee_2 = Programmer("Ashisa",200,"Stack Overflow")
employee_1.getDetails()
employee_2.getDetails()

