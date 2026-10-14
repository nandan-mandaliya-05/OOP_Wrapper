# OOP_Wrapper

 <div align="center">

# 👥 Employee Management System

### A Python-Based Object-Oriented Employee Management Program

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=26&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Employee+Management+System;Manage+Employees%2C+Managers+and+Developers;Python+%7C+OOP+%7C+Inheritance;Encapsulation+%7C+Method+Overriding;Console-Based+Management+System" alt="Animated Typing Header"/>

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Employee%20Management-00C2FF?style=for-the-badge)
![Application](https://img.shields.io/badge/Application-Console-success?style=for-the-badge)
![Concepts](https://img.shields.io/badge/Concepts-OOP-orange?style=for-the-badge)

<br>

</div>

---

# 🌟 About The Project

**Employee Management System** is a Python-based, menu-driven console application designed to manage employee information using Object-Oriented Programming (OOP).

The program supports three types of records:

- **Employee:** Stores name, age, employee ID, and salary.
- **Manager:** Inherits employee details and adds department information.
- **Developer:** Inherits employee details and adds programming language information.

The application demonstrates practical usage of **classes, objects, constructors, inheritance, encapsulation, getters and setters, method overriding, `super()`, lists, loops, conditional statements, and `issubclass()`**.

This project is designed to strengthen Python programming fundamentals and develop a practical understanding of Object-Oriented Programming.

> **"Organize employee information. Practise object-oriented programming. Build practical Python projects."**

---

# 🎯 Project Objectives

The main objectives of this project are:

- 👤 Create employee records.
- 🧑‍💼 Create manager records with department information.
- 💻 Create developer records with programming language information.
- 📋 Store multiple objects using Python lists.
- 🔐 Understand encapsulation through private attributes.
- 🔎 Access private attributes using getter methods.
- ✏️ Update private attributes using setter methods.
- 🧬 Implement inheritance using parent and child classes.
- ♻️ Practise method overriding.
- 🧰 Reuse parent-class functionality using `super()`.
- 🧪 Check inheritance relationships using `issubclass()`.
- 🏗️ Combine Python OOP concepts into a menu-driven application.

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 👤 Employee Creation

Create an employee with a name, age, employee ID, and salary.

</td>
<td width="50%">

### 🧑‍💼 Manager Creation

Create a manager with employee details and an additional department attribute.

</td>
</tr>
<tr>
<td width="50%">

### 💻 Developer Creation

Create a developer with employee details and a programming language.

</td>
<td width="50%">

### 📋 Display Details

Display stored employee, manager, and developer records separately.

</td>
</tr>
<tr>
<td width="50%">

### 🔐 Encapsulation

Use private attributes for employee ID and salary.

</td>
<td width="50%">

### 🧬 Inheritance Checking

Use `issubclass()` to verify the relationship between parent and child classes.

</td>
</tr>
</table>

---

# 🧰 Technology Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github" alt="Python, VS Code, Git and GitHub"/>

</div>

### Core Technologies

| Technology / Concept | Purpose |
|---|---|
| 🐍 Python | Application development |
| 🏛️ Classes and Objects | Represent employees and their roles |
| 🧱 `__init__()` | Initialize object attributes |
| 🧬 Inheritance | Reuse common employee functionality |
| 🔐 Encapsulation | Use private attributes for employee ID and salary |
| 🔎 Getters and Setters | Retrieve and update private attributes |
| ♻️ Method Overriding | Customize methods in child classes |
| 🧰 `super()` | Call parent-class methods and constructors |
| 📋 Lists | Store employee, manager, and developer objects |
| 🔁 Loops | Repeat menus and process records |
| 🔀 Conditional Statements | Handle user choices |
| 🧪 `issubclass()` | Check class inheritance relationships |
| 🖥️ Console Input/Output | Interact with the user through a terminal |

---

# 🏗️ Class Structure

The application uses one parent class and two child classes.

## 1. Employee Class

The `Employee` class is the parent class. It contains the common attributes and methods shared by the other classes.

### Attributes

| Attribute | Description |
|---|---|
| `name` | Stores the employee's name |
| `age` | Stores the employee's age |
| `__employee_id` | Stores the employee ID as a private attribute |
| `__salary` | Stores the employee's salary as a private attribute |

### Getter and Setter Methods

The class provides four methods for accessing and updating private attributes.

```python
def get_employee_id(self):
    return self.__employee_id

def set_employee_id(self, employee_id):
    self.__employee_id = employee_id

def get_salary(self):
    return self.__salary

def set_salary(self, salary):
    self.__salary = salary
```

- `get_employee_id()` returns the employee ID.
- `set_employee_id()` updates the employee ID.
- `get_salary()` returns the salary.
- `set_salary()` updates the salary.

The `display_details()` method displays the employee's name, age, employee ID, and salary.

## 2. Manager Class

The `Manager` class inherits from `Employee` and adds a `department` attribute.

```python
class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
```

### Concepts Demonstrated

- `Manager(Employee)` establishes inheritance.
- `super().__init__()` initializes the attributes inherited from `Employee`.
- `department` stores the manager's department.
- `display_details()` overrides the parent method and displays additional information.

## 3. Devloper Class

The program uses the class name `Devloper` in the source code.

The class inherits from `Employee` and adds a `programming_lang` attribute.

```python
class Devloper(Employee):

    def __init__(self, name, age, salary, employee_id, programming_lang):
        super().__init__(name, age, employee_id, salary)
        self.programming_lang = programming_lang

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_lang}")
```

### Concepts Demonstrated

- `Devloper(Employee)` establishes inheritance.
- `super()` reuses the parent-class constructor and display method.
- `programming_lang` stores the developer's programming language.
- `display_details()` overrides the parent method and displays additional information.

**Important implementation note:** In the current code, the `Devloper` constructor accepts `salary` before `employee_id`, but the object-creation statement passes `employee_id` before `salary`. This causes the two values to be assigned incorrectly. Make the constructor parameter order consistent with the call to fix this issue.

---

# 🧬 Inheritance Overview

The class hierarchy is:

```text
                  Employee
                 /        \
                /          \
           Manager        Devloper
              |               |
         Department     Programming Language
```

Both child classes inherit common attributes and methods from the `Employee` class.

| Class | Parent Class | Additional Attribute |
|---|---|---|
| `Employee` | None | Common employee details |
| `Manager` | `Employee` | `department` |
| `Devloper` | `Employee` | `programming_lang` |

Inheritance reduces code duplication by allowing child classes to reuse existing functionality.

---

# 🔐 Encapsulation in the Project

Encapsulation is demonstrated through the private attributes `__employee_id` and `__salary`.

```python
self.__employee_id = employee_id
self.__salary = salary
```

In Python, double underscores trigger name mangling, which helps prevent accidental direct access to these attributes through their original names.

The getter and setter methods provide a way to retrieve and update their values.

### Example

```python
emp = Employee("Aarav", 25, 101, 35000)

print(emp.get_employee_id())
print(emp.get_salary())

emp.set_employee_id(102)
emp.set_salary(40000)
```

Output:

```text
101
35000
```

After the setter calls, the employee ID becomes `102` and the salary becomes `40000`.

The current menu does not include a separate option for updating existing records, but the class provides the necessary setter methods.

---

# ♻️ Method Overriding and `super()`

Both child classes define their own `display_details()` method.

The parent class displays:

- Name
- Age
- Employee ID
- Salary

The `Manager` class additionally displays the department, while the `Devloper` class additionally displays the programming language.

The statement `super().display_details()` calls the parent-class method so the child class can reuse the common display logic before printing its additional information.

This demonstrates **method overriding and code reuse through inheritance**.

---

# 📋 Menu Options

When the program starts, it displays the following menu:

```text
~~~~~~~~~~~~~~~~~~~~ Employee Management System ~~~~~~~~~~~~~~~~~~~~

Select a option:
1. Create a Employee
2. Create a Manager
3. Create a Devloper
4. Show Details
5. Check Inharitance
6. Exit System

Enter your option:
```

| Option | Operation |
|---|---|
| 1 | Create an employee |
| 2 | Create a manager |
| 3 | Create a developer |
| 4 | Display details by category |
| 5 | Check inheritance relationships |
| 6 | Exit the program |

The application uses a `while True` loop to keep displaying the menu until the user selects option 6.

---

# 📥 1. Create an Employee

Choose option `1` to enter the employee's details.

### Example Input

```text
Enter your option: 1
Enter a name: Aarav
Enter a age: 25
Enter a Employee id: 101
Enter a salary: 35000

Employee created successfully.
```

The program creates an `Employee` object and stores it in the `employee` list.

```python
employ = Employee(name, age, employee_id, salary)
employee.append(employ)
```

The list can hold multiple employee objects during the current program session.

---

# 🧑‍💼 2. Create a Manager

Choose option `2` to enter the manager's details, including a department.

### Example Input

```text
Enter your option: 2
Enter a name: Diya
Enter a age: 32
Enter a Employee id: 201
Enter a salary: 60000
Enter a department: IT

Manager created successfully.
```

The manager object is stored in the `manager` list.

```python
manage = Manager(name, age, employee_id, salary, department)
manager.append(manage)
```

The manager's displayed details include all common employee information and the department.

---

# 💻 3. Create a Developer

Choose option `3` to enter the developer's details, including a programming language.

### Example Input

```text
Enter a name: Rohan
Enter a age: 27
Enter a Employee id: 301
Enter a salary: 50000
Enter a language: Python

Devloper created successfully.
```

The developer object is stored in the `devloper` list.

```python
devlop = Devloper(name, age, employee_id, salary, language)
devloper.append(devlop)
```

**Note:** The current constructor's parameter order must be corrected for the entered employee ID and salary to display properly.

---

# 📋 4. Show Details

Choose option `4` to display records from a selected category.

```text
Select a choice:
1. Employee
2. Manager
3. Devloper

Enter a choice:
```

The program checks whether the selected list contains any records. If records exist, a `for` loop iterates through the list and calls each object's `display_details()` method.

### Example Employee Output

```text
Employee Details:

Name: Aarav
Age: 25
Employee id: 101
Salary: ₹35000
```

### Example Manager Output

```text
Manager Details:

Name: Diya
Age: 32
Employee id: 201
Salary: ₹60000
Department: IT
```

### Example Developer Output

```text
Devloper Details:

Name: Rohan
Age: 27
Employee id: 301
Salary: ₹50000
Programming Language: Python
```

The developer output above assumes the constructor parameter order has been corrected.

---

# 🧪 5. Check Inheritance

Choose option `5` to verify that `Manager` and `Devloper` inherit from `Employee`.

```python
print("Manager class is subclass of employee:", issubclass(Manager, Employee))
print("Devloper class is subclass of employee:", issubclass(Devloper, Employee))
```

### Example Output

```text
Manager class is subclass of employee: True
Devloper class is subclass of employee: True
```

The built-in `issubclass()` function returns `True` when the first class is a subclass of the second class.

---

# 📦 Data Structures Used

The program uses three lists to store objects.

```python
employee = []
manager = []
devloper = []
```

| List | Stores |
|---|---|
| `employee` | `Employee` objects |
| `manager` | `Manager` objects |
| `devloper` | `Devloper` objects |

These lists exist in memory while the program is running. The current implementation does **not** save records to a file or database, so the records are lost when the program exits.

---

# 🧠 Python Concepts Practised

### 🏛️ Classes and Objects

Created classes representing employees and their specialized roles.

### 🧱 Constructors

Used `__init__()` to initialize object attributes.

### 🧬 Inheritance

Used `Manager(Employee)` and `Devloper(Employee)` to inherit common functionality.

### 🔐 Encapsulation

Used double-underscore attributes for employee ID and salary.

### 🔎 Getters and Setters

Created methods to retrieve and update private attribute values.

### ♻️ Method Overriding

Redefined `display_details()` in child classes to include role-specific information.

### 🧰 `super()`

Called parent-class constructors and methods from child classes.

### 📋 Lists and Objects

Stored multiple objects in lists and iterated through them to display records.

### 🔁 Loops and Conditional Statements

Used `while`, `for`, `if`, `elif`, and `else` to control program flow.

### 🧪 `issubclass()`

Checked inheritance relationships between classes.

---

# 📁 Project Structure

```text
PR-5 - OOP_Wrapper/
│
└── employee_management_system.py

README.md
```

**Note:** `Employee_management_system.py` is a suggested filename. Replace it with the actual name of your Python script if it is different.

---

# 🚀 How to Run the Project

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd PR-5 - OOP_Wrapper
```

### 3. Run the Python Program

```bash
python employee_management_system.py
```

If Python is installed and configured correctly, the Employee Management System menu will appear in your terminal.

### Requirements

- Python 3.x
- A terminal or command prompt
- A code editor such as Visual Studio Code (optional)

**External dependencies:** None. The program uses Python's built-in features and does not require external libraries.

---

# 🖥️ Example Application

```text
~~~~~~~~~~~~~~~~~~~~ Employee Management System ~~~~~~~~~~~~~~~~~~~~

Select a option:
1. Create a Employee
2. Create a Manager
3. Create a Devloper
4. Show Details
5. Check Inharitance
6. Exit System

Enter your option: 5

Manager class is subclass of employee: True
Devloper class is subclass of employee: True
```

This example demonstrates the inheritance-checking option. Actual output depends on the user's menu selections and the records created during the current run.

---

# 📈 Project Learning Outcomes

Through this project, I practised:

- 🐍 Python programming fundamentals
- 🏛️ Classes and objects
- 🧱 Constructors and instance attributes
- 🧬 Single inheritance
- 🔐 Encapsulation and private attributes
- 🔎 Getter and setter methods
- ♻️ Method overriding
- 🧰 The `super()` function
- 📋 Lists containing class objects
- 🔁 Loops and conditional statements
- 🧪 The `issubclass()` built-in function
- 🖥️ Building a menu-driven console application

---

# 🔮 Future Enhancements

The project can be extended with the following features:

- 🔍 Search for employees by ID or name.
- ✏️ Add menu options to update employee details.
- 🗑️ Delete employee, manager, or developer records.
- 🔐 Validate age, salary, and employee ID.
- 🛡️ Handle invalid numeric input using exception handling.
- 💾 Save and load records using JSON or a database.
- 🆔 Prevent duplicate employee IDs.
- 📊 Display employee counts and salary summaries.
- 🧩 Use a common employee registry for all employee types.
- 🖥️ Build a graphical user interface.
- 🌐 Convert the application into a web-based employee management system.

---

# 🗺️ Project Roadmap

```text
[████████████████████] 100% Employee Class
[████████████████████] 100% Manager Subclass
[████████████████████] 100% Devloper Subclass
[████████████████████] 100% Menu-Driven Record Creation
[████████████████████] 100% Display Employee Details
[████████████████████] 100% Inheritance Check
[░░░░░░░░░░░░░░░░░░░░]   0% Search and Update Menu
[░░░░░░░░░░░░░░░░░░░░]   0% Persistent File Storage
[░░░░░░░░░░░░░░░░░░░░]   0% Input Validation
[░░░░░░░░░░░░░░░░░░░░]   0% GUI
```

*Roadmap percentages are a suggested starting point based on the features in the supplied code. Update them as the project changes.*

---

# ⭐ Why I Built This Project

I created this project to strengthen my understanding of Python Object-Oriented Programming.

Instead of practising classes, inheritance, encapsulation, and method overriding separately, I combined these concepts into one interactive application.

This project helped me practise how to:

- Represent real-world roles using classes.
- Reuse code through inheritance.
- Protect selected attributes using encapsulation.
- Extend parent-class behavior through method overriding.
- Store and display multiple objects.
- Build an interactive menu using loops and conditional statements.

This project is part of my journey toward learning **Python, Data Science, and AI/ML**.

---

# 👨‍💻 About the Developer

<div align="center">

## Python Developer | Data Science and AI/ML Learner

Currently learning and building projects using:

```text
Python
  ↓
Object-Oriented Programming
  ↓
Data Structures and Problem Solving
  ↓
Data Analysis
  ↓
Data Science
  ↓
AI / ML
```

</div>

---

# 🌐 Connect With Me

<div align="center">

### GitHub

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nandan-mandaliya-05/)

</div>

---

# ⭐ Support the Project

If you find this project useful or interesting:

- ⭐ **Star** the repository.
- 🍴 **Fork** the repository.
- 💬 **Share** your feedback.
- 🤝 **Connect** with me on GitHub.

Your feedback and suggestions can help improve future versions of this project.

---

<div align="center">

# 🚀 Keep Learning. Keep Building. Keep Growing.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=750&lines=Python+%7C+Object-Oriented+Programming;Build+Projects+%7C+Learn+Concepts+%7C+Grow+Skills;Keep+Learning+%7C+Keep+Building" alt="Animated Footer"/>

<br><br>

**Made with ❤️ and Python by Nandan Mandaliya**

</div>