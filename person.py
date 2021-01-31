class Person:
    
    def __init__(self, firstname = "J.", lastname = "Doe", wage = 10.00, hours = 40.00):
        self.firstname = firstname
        self.lastname = lastname
        self.wage = wage
        self.hours = hours
        
    def getPerson(self):
        f = open("EmpData.txt", "a")
        firstname, lastname = input("Hello! What is your full name?: ").split(" ")
        self.firstname = firstname
        self.lastname = lastname
        f.write("\n")
        f.write(firstname)
        f.write(" ")
        f.write(lastname)
        f.write(", ")

    def getWages(self):
        f = open("EmpData.txt", "a")
        wage = input("What are employee's wages?: ")
        self.wage = wage
        f.write(wage)
        f.write(", ")

    def getHours(self):
        f = open("EmpData.txt", "a")
        hours = input("How many hours does employee work?: ")
        self.hours = hours
        f.write(hours)

    def setfirstname(self, firstname):
        self.firstname = firstname

    def setlastname(self, lastname):
        self.lastname = lastname