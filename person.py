class Person:
    
    def __init__(self, firstname = "J.", lastname = "Doe", wage = 10.00, hours = 40.00):
        self.firstname = firstname
        self.lastname = lastname
        self.wage = wage
        self.hours = hours
        
    def getPerson(self):
        f = open("EmpData.txt", "a")
        firstname, lastname = input("What is employee's full name?: ").split(" ")
        self.firstname = firstname
        self.lastname = lastname
        f.write("\n")
        f.write(firstname)
        f.write(" ")
        f.write(lastname)
        f.write(", ")
        f.close()

    def getWages(self):
        f = open("EmpData.txt", "a")
        wage = input("What are the employee's wages?: ")
        self.wage = wage
        f.write(wage)
        f.write(", ")
        f.close()

    def getHours(self):
        f = open("EmpData.txt", "a")
        hours = input("How many hours does the employee work?: ")
        self.hours = hours
        f.write(hours)
        #f.write("\n")
        f.close()
    
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

    def calcSalary(self):
        calc = input("Select an employee to calculate their salary: ")
        f = open("EmpData.txt", "r")
        lines = f.readlines()
        for line in lines:   
            if (line.startswith(calc)):
                parts = line.split(", ")
                wage = float(parts[1])
                hours = int(parts[2])
                weeks = int(input("How many weeks does the employee work?: "))
                print(calc, "\b's salary is $", wage * hours * weeks)
        f.close()

    def giveRaise(self):
        EmpRaise = input("Who would you like to give a raise to?: ")
        f = open("EmpData.txt", "r")
        lines = f.readlines()
        f.close()

        nf = open("EmpData.txt", "w")
        for line in lines:   
            if (line.startswith(EmpRaise)):
                parts = line.split(", ")
                wage = (parts[1])
                newWage = (input("What is the employee's new pay?: "))
                nf.write(line.replace(wage, newWage))
                print(EmpRaise, "\b's wages are now $", newWage)
            if not (line.startswith(EmpRaise)):
                nf.write(line)
        nf.close()
    
    def changeHours(self):
        EmpHours = input("Who's hours are being changed?: ")
        f = open("EmpData.txt", "r")
        lines = f.readlines()
        f.close()

        nf = open("EmpData.txt", "w")
        for line in lines:   
            if (line.startswith(EmpHours)):
                parts = line.split(", ")
                hours = (parts[2])
                newHours = (input("What are the employee's new hours?: "))
                nf.write(line.replace(hours, newHours))
                print(EmpHours, "now works ", newHours, "a week.")
            if not (line.startswith(EmpHours)):
                nf.write(line)
        nf.close()

    def setfirstname(self, firstname):
        self.firstname = firstname

    def setlastname(self, lastname):
        self.lastname = lastname