# OOP_Wrapper
::: {align="center"}
# 👨‍💼 Employee Management System

### A Python-Based Object-Oriented Employee Management Application

`<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=25&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Employee+Management+System;Manage+Employees%2C+Managers+and+Developers;Python+%7C+OOP+%7C+Inheritance;Encapsulation+%7C+Method+Overriding;Console-Based+Management+Application" alt="Animated Typing Header"/>`{=html}

`<br>`{=html}

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Project](https://img.shields.io/badge/Project-Employee%20Management-00C2FF?style=for-the-badge)
![Application](https://img.shields.io/badge/Application-Console-success?style=for-the-badge)
![OOP](https://img.shields.io/badge/Concept-Object--Oriented-purple?style=for-the-badge)

`<br>`{=html}
:::

------------------------------------------------------------------------

# 🌟 About The Project

**Employee Management System** is a Python-based console application
designed to create and display information about different types of
employees.

The application supports three classes of people in an organization:
**Employee, Manager, and Developer**. Managers and developers inherit
common employee information from the parent `Employee` class and add
their own role-specific details.

The program uses a menu-driven interface that allows users to create
records, display stored details, and check inheritance relationships.

This project demonstrates practical use of Python **Classes, Objects,
Constructors, Encapsulation, Getters, Setters, Inheritance, `super()`,
Method Overriding, Lists, Loops, Conditional Statements, and
`issubclass()`**.

It is a learning project created to strengthen understanding of
Object-Oriented Programming (OOP) in Python.

> **"Build reusable classes. Protect data. Understand object-oriented
> programming."**

------------------------------------------------------------------------

# 🎯 Project Objectives

The main objectives of this project are:

-   👤 Create employee records with name, age, employee ID, and salary.
-   🧑‍💼 Create managers with an additional department field.
-   💻 Create developers with an additional programming-language field.
-   🔐 Practise encapsulation using private attributes.
-   🔎 Access and update private attributes using getter and setter
    methods.
-   🧬 Reuse employee attributes through inheritance.
-   ♻️ Call parent-class methods using `super()`.
-   🛠️ Override methods to display role-specific information.
-   📋 Store multiple objects in Python lists.
-   🧪 Check inheritance relationships using `issubclass()`.
-   🏗️ Combine OOP concepts in a menu-driven console application.

------------------------------------------------------------------------

# ✨ Key Features

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
### 👤 Create Employee

Enter a name, age, employee ID, and salary to create an employee object.

```{=html}
</td>
```
```{=html}
<td width="50%">
```
### 🧑‍💼 Create Manager

Create a manager record with common employee details and a department.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
### 💻 Create Developer

Create a developer record with common employee details and a programming
language.

```{=html}
</td>
```
```{=html}
<td width="50%">
```
### 📋 Display Details

Display the saved records for employees, managers, or developers
separately.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td width="50%">
```
### 🔐 Encapsulation

Keep employee ID and salary in private attributes and provide getter and
setter methods.

```{=html}
</td>
```
```{=html}
<td width="50%">
```
### 🧬 Inheritance Check

Use `issubclass()` to check whether the manager and developer classes
inherit from `Employee`.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```

------------------------------------------------------------------------

# 🧰 Technology Stack

::: {align="center"}
`<img src="https://skillicons.dev/icons?i=python,vscode,git,github" alt="Python, VS Code, Git and GitHub"/>`{=html}
:::

### Core Technologies

  -----------------------------------------------------------------------
  Technology / Concept                Purpose
  ----------------------------------- -----------------------------------
  🐍 Python 3.x                       Application development

  🧱 Classes and Objects              Model employees and their
                                      specialized roles

  🏗️ `__init__()`                     Initialize object attributes

  🔐 Encapsulation                    Keep selected attributes private

  🔎 Getters and Setters              Read and update private attributes

  🧬 Inheritance                      Reuse the `Employee` class in child
                                      classes

  ♻️ `super()`                        Call parent-class methods and
                                      constructors

  🛠️ Method Overriding                Customize `display_details()` in
                                      child classes

  📋 Lists                            Store multiple objects by role

  🔁 `while` and `for` loops          Repeat the menu and display records

  🔀 Conditional Statements           Handle menu selections

  🧪 `issubclass()`                   Check inheritance relationships

  ⌨️ `input()` and `print()`          Interact with the user through the
                                      terminal
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 🏗️ Class Structure

The project contains one parent class and two child classes.

## 1. Employee Class

The `Employee` class is the parent class. It stores the common
information shared by all employee types.

``` python
class Employee:

    def __init__(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary
```

### Attributes

  Attribute         Description
  ----------------- ---------------------
  `name`            Employee's name
  `age`             Employee's age
  `__employee_id`   Private employee ID
  `__salary`        Private salary

The class also defines getter and setter methods for the private
attributes, along with `display_details()` to display the employee
information.

## 2. Manager Class

The `Manager` class inherits from `Employee` and adds a `department`
attribute.

``` python
class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")
```

The `super()` function initializes the common employee attributes and
reuses the parent class's display method.

## 3. Developer Class

The code currently names this class `Devloper`. It inherits from
`Employee` and adds a `programming_lang` attribute.

``` python
class Devloper(Employee):

    def __init__(self, name, age, salary, employee_id, programming_lang):
        super().__init__(name, age, employee_id, salary)
        self.programming_lang = programming_lang

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_lang}")
```

**Naming note:** `Devloper` is the spelling used in the current source
code. You can rename it to `Developer` consistently throughout the
program for conventional spelling.

------------------------------------------------------------------------

# 🧬 Inheritance Overview

The `Manager` and `Devloper` classes inherit from the `Employee` class.

``` text
                 Employee
                    |
             +------+------+
             |             |
          Manager       Devloper
             |             |
         Department   Programming Language
```

### Inheritance Relationships

  Parent Class   Child Class   Relationship
  -------------- ------------- ------------------------------------
  `Employee`     `Manager`     Manager is a subclass of Employee
  `Employee`     `Devloper`    Devloper is a subclass of Employee

The program verifies these relationships with:

``` python
print(issubclass(Manager, Employee))
print(issubclass(Devloper, Employee))
```

Expected output:

``` text
True
True
```

------------------------------------------------------------------------

# 🔐 Encapsulation: Getters and Setters

The employee ID and salary are stored using double-underscore attribute
names:

``` python
self.__employee_id = employee_id
self.__salary = salary
```

Getter methods return the values:

``` python
def get_employee_id(self):
    return self.__employee_id

def get_salary(self):
    return self.__salary
```

Setter methods update the values:

``` python
def set_employee_id(self, employee_id):
    self.__employee_id = employee_id

def set_salary(self, salary):
    self.__salary = salary
```

These methods demonstrate controlled access to attributes. The current
menu does not yet provide an option for updating an existing record; the
setters are available to be called directly from Python code.

------------------------------------------------------------------------

# 🛠️ Method Overriding

All employee types share the `display_details()` method, but managers
and developers need to display additional information.

The child classes override the method and call the parent's version
using `super()`.

``` python
def display_details(self):
    super().display_details()
    print(f"Department: {self.department}")
```

For a developer, the additional field is the programming language.

This approach avoids rewriting the common employee details in every
subclass.

------------------------------------------------------------------------

# 📋 Menu Options

When the program starts, it displays the following menu:

``` text
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

  Option   Action
  -------- -----------------------------------------------------
  1        Create an Employee
  2        Create a Manager
  3        Create a Developer (`Devloper` in the current code)
  4        Show saved details by role
  5        Check inheritance relationships
  6        Exit the system

The `while` loop keeps displaying the menu until the user selects option
6.

------------------------------------------------------------------------

# 👤 1. Create an Employee

Choose option 1 and enter the employee's details.

### Example Input

``` text
Enter a name: Rahul
Enter a age: 25
Enter a Employee id: 101
Enter a salary: 35000

Employee created successfully.
```

### Example Display

``` text
Employee Details:

Name: Rahul
Age: 25
Employee id: 101
Salary: ₹35000
```

The newly created object is stored in the `employee` list.

``` python
employee = []

employ = Employee(name, age, employee_id, salary)
employee.append(employ)
```

------------------------------------------------------------------------

# 🧑‍💼 2. Create a Manager

Choose option 2 to create a manager. In addition to common employee
details, enter the manager's department.

### Example Input

``` text
Enter a name: Priya
Enter a age: 32
Enter a Employee id: 201
Enter a salary: 60000
Enter a department: IT

Manager created successfully.
```

### Example Display

``` text
Name: Priya
Age: 32
Employee id: 201
Salary: ₹60000
Department: IT
```

The manager object is stored in the `manager` list.

``` python
manager = []

manage = Manager(name, age, employee_id, salary, department)
manager.append(manage)
```

------------------------------------------------------------------------

# 💻 3. Create a Developer

Choose option 3 to create a developer. The additional field records the
programming language.

### Example Input

``` text
Enter a name: Arjun
Enter a age: 27
Enter a Employee id: 301
Enter a salary: 50000
Enter a language: Python

Devloper created successfully.
```

### Example Display

``` text
Name: Arjun
Age: 27
Employee id: 301
Salary: ₹50000
Programming Language: Python
```

The developer object is stored in the `devloper` list.

``` python
devloper = []

devlop = Devloper(name, age, employee_id, salary, language)
devloper.append(devlop)
```

------------------------------------------------------------------------

# 📋 4. Show Details

Option 4 opens a second menu:

``` text
Select a choice:
1. Employee
2. Manager
3. Devloper

Enter a choice:
```

The program checks the selected list and displays every stored object of
that role.

Example:

``` python
for emp in employee:
    emp.display_details()
    print()
```

The same pattern is used for manager and developer objects.

If a list is empty, the program displays a message instead of trying to
display records that do not exist.

------------------------------------------------------------------------

# 🧪 5. Check Inheritance

Option 5 uses Python's built-in `issubclass()` function.

``` python
print(
    "Manager class is subclass of employee:",
    issubclass(Manager, Employee)
)

print(
    "Devloper class is subclass of employee:",
    issubclass(Devloper, Employee)
)
```

### Expected Output

``` text
Manager class is subclass of employee: True
Devloper class is subclass of employee: True
```

Both results are `True` because the two classes inherit from `Employee`.

------------------------------------------------------------------------

# 🔄 Application Workflow

``` text
              +----------------------+
              |        START         |
              +----------+-----------+
                         |
              +----------v-----------+
              |     Display Menu     |
              +----------+-----------+
                         |
              +----------v-----------+
              |    Enter Choice      |
              +----------+-----------+
                         |
        +----------------+----------------+
        |                |                |
   Create Employee  Show Details    Check Inheritance
        |                |                |
   +----+-----+     Select Role       issubclass()
   |          |          |                |
 Employee  Manager /  Display Stored      Show Result
           Devloper      Objects
        |                |
        +----------------+
                         |
              +----------v-----------+
              |   Continue Menu?     |
              +----------+-----------+
                         |
                 Exit when selected
                         |
              +----------v-----------+
              |         END          |
              +----------------------+
```

------------------------------------------------------------------------

# 📁 Project Structure

``` text
Employee-Management-System/
│
├── employee_management.py
└── README.md
```

**Note:** `employee_management.py` is a suggested filename. Use the
actual filename of your Python script when running the program.

This project uses Python's built-in features and requires no external
libraries.

------------------------------------------------------------------------

# 🚀 How to Run the Project

### 1. Clone the Repository

Replace the placeholder with your GitHub repository URL.

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

``` bash
cd Employee-Management-System
```

### 3. Run the Python Program

``` bash
python employee_management.py
```

If Python is installed and configured correctly, the Employee Management
System menu will appear in the terminal.

### Requirements

-   Python 3.x
-   Terminal or command prompt
-   A code editor such as Visual Studio Code (optional)

------------------------------------------------------------------------

# 🧠 Python Concepts Practised

### 🧱 Classes and Objects

Created objects from the `Employee`, `Manager`, and `Devloper` classes.

### 🏗️ Constructors

Used `__init__()` to initialize each object's attributes.

### 🔐 Encapsulation

Used private attributes for employee ID and salary, with getter and
setter methods.

### 🧬 Inheritance

Reused the common attributes and methods of the `Employee` class in
child classes.

### ♻️ `super()`

Called the parent constructor and parent display method from child
classes.

### 🛠️ Method Overriding

Customized `display_details()` for managers and developers.

### 📋 Lists of Objects

Stored multiple records in separate lists and iterated through them to
display details.

### 🔁 Loops

Used a `while` loop for the main menu and `for` loops to display
records.

### 🔀 Conditional Statements

Used `if`, `elif`, and `else` to process menu choices.

### 🧪 Built-in Functions

Used `len()` to check whether a list contains records and `issubclass()`
to check inheritance.

------------------------------------------------------------------------

# 📈 Project Learning Outcomes

Through this project, I practised:

-   🐍 Python programming fundamentals.
-   🧱 Designing classes and creating objects.
-   🏗️ Initializing objects with constructors.
-   🔐 Implementing encapsulation with private attributes.
-   🔎 Creating getter and setter methods.
-   🧬 Applying inheritance to reduce code duplication.
-   ♻️ Reusing parent class methods with `super()`.
-   🛠️ Overriding methods in child classes.
-   📋 Storing and managing objects in lists.
-   🔁 Building a repeating menu with loops.
-   🧪 Checking class relationships with `issubclass()`.
-   🏗️ Combining OOP concepts into a practical console application.

------------------------------------------------------------------------

# ⚠️ Current Limitations

The current version is designed for practising OOP concepts. It has the
following limitations:

-   💾 Records are stored only in memory and are lost when the program
    exits.
-   ✏️ The menu does not yet include update or delete operations.
-   🔍 There is no employee search feature.
-   🛡️ Invalid numeric input can cause an error because input validation
    is limited.
-   🆔 Duplicate employee IDs are not checked.
-   🔐 The getter and setter methods are implemented, but there is no
    menu option to use them.
-   📝 The class name `Devloper` and some menu text contain spelling
    errors.

------------------------------------------------------------------------

# 🔮 Future Enhancements

The project can be improved with the following features:

-   🔎 Search employees by ID or name.
-   ✏️ Update existing employee information.
-   🗑️ Delete employee records.
-   💾 Save and load records using JSON or CSV.
-   🗄️ Store employee data in a database such as SQLite.
-   🆔 Prevent duplicate employee IDs.
-   🛡️ Add input validation and exception handling.
-   💰 Validate salary and age values.
-   📊 Generate employee and department reports.
-   🧹 Rename `Devloper` to `Developer` throughout the program.
-   🖥️ Build a graphical user interface.
-   🌐 Convert the application into a web-based employee management
    system.

------------------------------------------------------------------------

# 🗺️ Project Roadmap

``` text
[████████████████████] 100% Employee Class

[████████████████████] 100% Manager Subclass

[████████████████████] 100% Developer Subclass
                       (named Devloper in current code)

[████████████████████] 100% Encapsulation and Accessor Methods

[████████████████████] 100% Method Overriding

[████████████████████] 100% Menu-Driven Record Creation

[████████████████████] 100% Display Records by Role

[████████████████████] 100% Inheritance Checking

[░░░░░░░░░░░░░░░░░░░░]   0% Search, Update and Delete

[░░░░░░░░░░░░░░░░░░░░]   0% Persistent Data Storage

[░░░░░░░░░░░░░░░░░░░░]   0% Database Integration

[░░░░░░░░░░░░░░░░░░░░]   0% Graphical User Interface
```

*Roadmap percentages reflect the features present in the code shared for
this README. Update them as the project evolves.*

------------------------------------------------------------------------

# ⭐ Why I Built This Project

I created this project to strengthen my understanding of Python
Object-Oriented Programming.

Instead of practising each concept separately, I combined classes,
encapsulation, inheritance, method overriding, and object collections
into one interactive application.

This project helped me understand how a parent class can provide common
functionality while child classes add their own specialized information.

It is part of my journey toward becoming a stronger Python programmer
and building practical software projects.

------------------------------------------------------------------------

# 👨‍💻 About the Developer

::: {align="center"}
## Python Developer \| Data Science and AI/ML Learner

Currently learning and building projects using:

``` text
Python
  ↓
Data Structures
  ↓
Object-Oriented Programming
  ↓
Problem Solving
  ↓
Data Science
  ↓
AI / ML
```
:::

------------------------------------------------------------------------

# 🌐 Connect With Me

::: {align="center"}
### GitHub

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nandan-mandaliya-05/)
:::

------------------------------------------------------------------------

# ⭐ Support the Project

If you find this project useful or interesting:

-   ⭐ **Star** the repository.
-   🍴 **Fork** the repository.
-   💬 Share your feedback and suggestions.
-   🤝 Connect with me on GitHub.

Your feedback and suggestions can help improve future versions of this
project.

------------------------------------------------------------------------

::: {align="center"}
# 🚀 Keep Learning. Keep Building. Keep Growing.

`<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=750&lines=Python+%7C+OOP+%7C+Problem+Solving;Build+Projects+%7C+Learn+Concepts+%7C+Grow+Skills;Keep+Learning+%7C+Keep+Building" alt="Animated Footer"/>`{=html}

`<br>`{=html}`<br>`{=html}

**Made with ❤️ and Python by Nandan Mandaliya**
:::
