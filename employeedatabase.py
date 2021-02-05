import person

running = True

while (running):
    print("Options: 1: add employee, 2: remove employee, 3: calculate salary, 4: give raise, 5: change hours, 6: Exit")
    check = input("Please select an option. ")
    if (check == "1"):
        #Add employee
        you = person.Person()
        you.getPerson()
        you.getWages()
        you.getHours()
        print("The employee has been added to the database.")

    if (check == "2"):
        #Remove employee
        you = person.Person()
        you.removeEmp()
    
    if (check == "3"):
        #calculate salary
        #Specific person: Hourly from txt, Weekly hours from txt, Need number workweeks from input? Wage * Hours * Weeks = Salary
        you = person.Person()
        you.calcSalary()

    if (check == "4"):
        #give raise
        #replace specific wage in EmpData
        you = person.Person()
        you.giveRaise()

    if (check == "5"):
        #Change hours
        you = person.Person()
        you.changeHours()

    if (check == "6"):
        print("Goodbye!")
        quit()