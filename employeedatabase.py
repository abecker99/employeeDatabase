import person

running = True
employee = []
wage = []
hours = []
weeks = []
while (running):
    print("Options: 1: add employee, 2: remove employee, 3: calculate wages, 4: give raise, 5: Exit")
    check = input("Please select an option. ")
    if (check == "1"):
        you = person.Person()
        you.getPerson()
        you.getWages()
        you.getHours()

    if (check == "2"):
        you = person.Person()
        you.removeEmp()
    
    if (check == "3"):
        #calculate salary
        #Specific person: Hourly from txt, Weekly hours from txt, Need Workweek from input? Wage * Hours * Weeks = Salary
        calc = input("Pick employee: ")
        f = open("EmpData.txt", "r")
        lines = f.readlines()
        for line in lines:   
            if (line.startswith(calc)):
                parts = line.split(", ")
                wage = float(parts[1])
                hours = int(parts[2])
                weeks = int(input("How many weeks does employee work?: "))
                print(calc, "\b's salary is $", wage * hours * weeks)
        f.close()

    #if (check == "4"):
        #give raise
        #somehow replace specific wage in EmpData

    if (check == "5"):
        print("Goodbye!")
        quit()