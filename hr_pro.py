import datetime

class Employee:

    def __init__(self , name , age , salary , employment_year):
       self.name = name
       self.age  = age
       self.salary = int(salary)
       self.employment_year = employment_year

    def get_working_years(self, employment_year):
        today = datetime.date.today().year - 1
        return today - employment_year

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years(self.employment_year)}"




class Manager(Employee):
    #Manager class here
    def __init__(self, name , age , salary , employment_year , bonus_percentage):
        super().__init__(name , age , salary , employment_year)
        self.bonus_percentage = float(bonus_percentage)



    def get_bonus(self,bonus_percentage,salary):
        return bonus_percentage * salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working Years: {self.get_working_years(self.employment_year)}, Bonus: {self.get_bonus(self.bonus_percentage,self.salary)}"





def main():
    # main code here
    employees_list = []
    managers_list = []


    print("Welcome to HR Pro 2019")

    while True:
        #employee_list = employees_list.copy()
        #manager_list = managers_list.copy()
        print(("""Options:
                1. Show Employees
                2. Show Managers
                3. Add An Employee
                4. Add A Manager
                5. Exit"""))
        print()

        user_input = input("What would you like to do? ")
        print("-----------------")

        if user_input == "5":
            break

        if user_input == "3":
            name = input("Name: ")
            age  = input("Age: ")
            salary = int(input("Salary: "))
            employment_year = int(input("Employment year: "))
            employee = Employee(name,age , salary,employment_year)
            employees_list.append(employee)
            print("Employee added succesfully")

        elif user_input == "1":
            print("Employees")
            print()
            for empl in employees_list:
                print(empl.__str__())
            print("-----------------")



        elif user_input == "4":
            name = input("Name: ")
            age  = input("Age: ")
            salary = int(input("Salary: "))
            employment_year = int(input("Employment year: "))
            bonus_percentage = float(input("Bonus Percentage: "))
            manager = Manager(name,age , salary,employment_year,bonus_percentage)
            managers_list.append(manager)
            print("Manager added succesfully")

        elif user_input == "2":
            print("Managers")
            print()
            for managers in managers_list:
                print(managers.__str__())
            print("-----------------")

        print()



if __name__ == '__main__':
    main()
