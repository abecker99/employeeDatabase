class Person:
    
    def __init__(self, firstname = "J.", lastname = "Doe", wage = 10.00, hours = 40.00):
        self.firstname = firstname
        self.lastname = lastname
        self.wage = wage
        self.hours = hours
        
    def getPerson(self):
        firstname, lastname = input("Hello! What is your full name?: ").split(" ")
        self.firstname = firstname
        self.lastname = lastname

    def getWages(self):
        wage = input("Wages?: ")
        self.wage = wage

    def getHours(self):
        hours = input("How many hours does employee work?: ")
        self.hours = hours

    def setfirstname(self, firstname):
        self.firstname = firstname

    def setlastname(self, lastname):
        self.lastname = lastname