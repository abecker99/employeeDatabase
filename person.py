class Person:
    
    def __init__(self, firstname = "J.", lastname = "Doe", wage = 10.00, hours = 40.00):
        self.firstname = firstname
        self.lastname = lastname
        self.wage = wage
        self.hours = hours
        
    def getPerson(self):
        f = open("EmpData.txt", "a")
        firstname, lastname = input("Hello! What is employee's full name?: ").split(" ")
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
    
    def removeEmp(self):
        f = open("EmpData.txt", "r")
        lines = f.readlines()
        f.close()

        nf = open("EmpData.txt", "w")
        delEmp = input("Which employee would you like to remove?: ")
        for line in lines:   
            if not (line.startswith(delEmp)):
                print(line)
                nf.write(line)
        nf.close()

    def setfirstname(self, firstname):
        self.firstname = firstname

    def setlastname(self, lastname):
        self.lastname = lastname