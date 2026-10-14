class Employee:
    
    def __init__(self , name , age, employee_id, salary):
        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary
        
    def get_employee_id(self):
        return self.__employee_id
    
    def set_employee_id(self,employee_id):
        self.__employee_id = employee_id
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        self.__salary = salary
        
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee id: {self.__employee_id}")
        print(f"Salary: ₹{self.__salary}")
        
class Manager(Employee):
    
    def __init__(self , name ,age,employee_id, salary, department):
        super().__init__(name,age,employee_id,salary)
        self.department = department
        
    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
        
class Devloper(Employee):
    
    def __init__(self,name,age,salary,employee_id,programming_lang):
        super().__init__(name,age,employee_id,salary)
        self.programming_lang = programming_lang
        
    def display_details(self):
        super().display_details() 
        print(f"Programming Language: {self.programming_lang}")
       

employee = []
manager = []
devloper = []

while True:
    print("\n","~"*20,"Employee Management System","~"*20)
    
    print("\nSelect a option:")
    print("1. Create a Employee")
    print("2. Create a Manager")
    print("3. Create a Devloper")
    print("4. Show Details")
    print("5. Check Inharitance")
    print("6. Exit System")
    
    option = input("\nEnter your option:").strip()
    
    if option == "1":
        
        name = input("Enter a name:")
        age = int(input("Enter a age:"))
        employee_id = int(input("Enter a Employee id:"))
        salary = int(input("Enter a salary"))
        
        employ = Employee(name,age,employee_id,salary)
        employee.append(employ)
        print("\nEmployee created successfully.")
        
    elif option == "2":
        
        name = input("Enter a name:")
        age = int(input("Enter a age:"))
        employee_id = int(input("Enter a Employee id:"))
        salary = int(input("Enter a salary"))
        department = input("Enter a department:")
        
        manage = Manager(name,age,employee_id,salary,department)
        manager.append(manage)
        print("\nManager created successfully.")
        
    elif option == "3":
        name = input("Enter a name: ")
        age = int(input("Enter a age: "))
        employee_id = int(input("Enter a Employee id: "))
        salary = int(input("Enter a salary: ")) 
        language = input("Enter a language: ")
        
        devlop = Devloper(name,age,employee_id,salary,language)
        devloper.append(devlop)
        print("\nDevloper created successfully.")
        
    elif option == "4":
        
        print("\nSelect a choice:")
        print("1. Employee")
        print("2. Manager")
        print("3. Devloper")
        
        choice = input("\nEnter a choice:")

        if choice == "1":
            if len(employee) == 0:
                print("Employees not exist so please input details by option 2.")
                
            else:
                print(f"\nEmployee Details:\n")
                for emp in employee:
                    emp.display_details()
                    print()

        elif choice == "2":
            if len(manager)==0:
                print("Managers not exist so please input details by option 2.")
                
            else:
                print(f"\nManager Details:\n")
                for manag in manager:
                    manag.display_details()
                    print()

        elif choice == "3":
            if len(devloper) == 0:
                print("Devlopers not exist so please input details by option 3.")
                
            else:
                print(f"\nDevloper Details:\n")
                for dev in devloper:
                    dev.display_details() 
                    print()
                    
    elif option == "5":
        print("\nManager class is subclass of employee:",issubclass(Manager,Employee))
        print("Devloper class is subclass of employee:",issubclass(Devloper,Employee))
        
    elif option == "6":
        print("\nThank you.")
        exit()
    
    else:
        print("\nInvalid choice. Please input between 1 to 6.")
                
    
    
    
               
        