import person

running = True
employee = []
wage = []
hour = []
while (running):
    print("Options: 1: add employee, 2: remove employee, 3: calculate wages, 4: give raise, 5: Exit")
    check = input("Please select an option. ")
    if (check == "1"):
        you = person.Person()
        you.getPerson()
        employee.append(you)
        you.getWages()
        wage.append(you)
        you.getHours()
        hour.append(you)

    if (check == "2"):
        you = person.Person()
        you.removeEmp()
    
    if (check == "3"):
        #calculate salary
        #Specific person: Hourly from txt, Weekly hours from txt, Need Workweek from input? Wage * Hours * Weeks = Salary

    if (check == "4"):
        #give raise
        #somehow replace specific wage in EmpData

    if (check == "5"):
        quit()