# OOP_Wrapper
<div align="center">

# 👨‍💼 Employee Management System

### A Python-Based Object-Oriented Programming Project

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=25&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=850&lines=Employee+Management+System;Manage+Employees%2C+Managers+and+Developers;Python+%7C+OOP+%7C+Inheritance;Encapsulation+%7C+Method+Overriding" alt="Animated Employee Management System header" />

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Application](https://img.shields.io/badge/Application-Console-blue?style=for-the-badge)
![OOP](https://img.shields.io/badge/Concept-Object--Oriented-purple?style=for-the-badge)

</div>

------------------------------------------------------------------------

## 🌟 About the Project

**Employee Management System** is a menu-driven Python console
application created to practise Object-Oriented Programming (OOP).

The program lets users create and display three types of records:

- **Employee** — name, age, employee ID, and salary
- **Manager** — employee details plus a department
- **Developer** — employee details plus a programming language

The `Manager` and `Devloper` classes inherit common attributes and
methods from `Employee`. The program also demonstrates encapsulation,
getters and setters, `super()`, method overriding, lists of objects, and
`issubclass()`.

> **Project focus:** Practise core OOP concepts by combining them in one
> interactive Python program.

## 🎯 Project Objectives

- Create Employee, Manager, and Developer objects.
- Store and display multiple records for each role.
- Use private attributes for employee ID and salary.
- Practise getter and setter methods.
- Reuse common functionality through inheritance.
- Override `display_details()` to show role-specific information.
- Check inheritance relationships using `issubclass()`.
- Build a menu that repeats until the user exits.

## ✨ Features

| Feature              | Description                                         |
|----------------------|-----------------------------------------------------|
| 👤 Create Employee   | Add name, age, employee ID, and salary.             |
| 🧑‍💼 Create Manager    | Add employee details and a department.              |
| 💻 Create Developer  | Add employee details and a programming language.    |
| 📋 Display Details   | Display records separately by role.                 |
| 🔐 Encapsulation     | Store employee ID and salary in private attributes. |
| 🧬 Inheritance       | Reuse the `Employee` class in child classes.        |
| 🛠️ Method Overriding | Display role-specific fields in child classes.      |
| 🧪 Inheritance Check | Check class relationships with `issubclass()`.      |

## 🧰 Technology and Concepts

<figure>
<img
src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white"
alt="Python" />
<figcaption aria-hidden="true">Python</figcaption>
</figure>

| Concept                 | How it is used                                         |
|-------------------------|--------------------------------------------------------|
| Classes and objects     | Represent employees and their roles.                   |
| `__init__()`            | Initialize object attributes.                          |
| Encapsulation           | Use `__employee_id` and `__salary` private attributes. |
| Getters and setters     | Read and update private attributes.                    |
| Inheritance             | `Manager(Employee)` and `Devloper(Employee)`.          |
| `super()`               | Call the parent constructor and display method.        |
| Method overriding       | Customize `display_details()` in child classes.        |
| Lists                   | Keep collections of employee objects in memory.        |
| `while` and `for` loops | Repeat the menu and display records.                   |
| `issubclass()`          | Check inheritance relationships.                       |

## 🏗️ Class Structure

The application has one parent class and two child classes.

``` text
                 Employee
                    |
             +------+------+
             |             |
          Manager       Devloper
             |             |
        Department    Programming Language
```

### 1. `Employee`

The parent class stores the common information shared by all roles.

| Attribute       | Description         |
|-----------------|---------------------|
| `name`          | Employee’s name     |
| `age`           | Employee’s age      |
| `__employee_id` | Private employee ID |
| `__salary`      | Private salary      |

It also defines `get_employee_id()`, `set_employee_id()`,
`get_salary()`, `set_salary()`, and `display_details()`.

### 2. `Manager`

`Manager` inherits from `Employee` and adds the `department` attribute.
Its `display_details()` method calls the parent method with `super()`
and then displays the department.

### 3. `Devloper` (Developer)

The current source code uses the class name `Devloper`. It inherits from
`Employee` and adds `programming_lang`. Its `display_details()` method
also calls the parent method before displaying the programming language.

**Naming note:** If you rename `Devloper` to `Developer`, update every
occurrence of the class name in the code.

## 🔐 Encapsulation: Getters and Setters

The employee ID and salary use double-underscore attributes:

``` python
self.__employee_id = employee_id
self.__salary = salary
```

Getter methods return the values, while setter methods update them:

``` python
def get_employee_id(self):
    return self.__employee_id

def set_employee_id(self, employee_id):
    self.__employee_id = employee_id

def get_salary(self):
    return self.__salary

def set_salary(self, salary):
    self.__salary = salary
```

These methods are defined in the class, but the current menu does not
provide an option to update an existing record.

## 🛠️ Inheritance and Method Overriding

Both child classes inherit from `Employee` and override
`display_details()` to add their own information.

For example, the manager method follows this pattern:

``` python
def display_details(self):
    super().display_details()
    print(f"Department: {self.department}")
```

The developer class uses the same approach to display
`programming_lang`.

The inheritance relationship is checked with:

``` python
print(issubclass(Manager, Employee))
print(issubclass(Devloper, Employee))
```

Expected output:

``` text
True
True
```

## 📋 Menu Options

``` text
~~~~~~~~~~~~~~~~~~~~ Employee Management System ~~~~~~~~~~~~~~~~~~~~

Select a option:
1. Create a Employee
2. Create a Manager
3. Create a Devloper
4. Show Details
5. Check Inharitance
6. Exit System
```

| Option | Action                                              |
|--------|-----------------------------------------------------|
| 1      | Create an Employee                                  |
| 2      | Create a Manager                                    |
| 3      | Create a Developer (`Devloper` in the current code) |
| 4      | Display details by role                             |
| 5      | Check inheritance                                   |
| 6      | Exit the application                                |

The `while` loop repeats the menu until option 6 is selected.

## ▶️ Example Output

### Employee

``` text
Employee created successfully.

Employee Details:

Name: Rahul
Age: 25
Employee id: 101
Salary: ₹35000
```

### Manager

``` text
Manager created successfully.

Name: Priya
Age: 32
Employee id: 201
Salary: ₹60000
Department: IT
```

### Developer

``` text
Devloper created successfully.

Name: Arjun
Age: 27
Employee id: 301
Salary: ₹50000
Programming Language: Python
```

*The names and values above are examples to illustrate the program’s
output format.*

## 🔄 Application Workflow

``` text
          +------------------+
          |      START       |
          +--------+---------+
                   |
          +--------v---------+
          |   Display Menu   |
          +--------+---------+
                   |
          +--------v---------+
          |  Enter Option    |
          +--------+---------+
                   |
       +-----------+------------+
       |           |            |
   Create Role  Show Details  Check Inheritance
       |           |            |
       +-----------+------------+
                   |
          +--------v---------+
          | Repeat or Exit   |
          +--------+---------+
                   |
                  END
```

## 📁 Project Structure

``` text
Employee-Management-System/
├── employee_management.py
└── README.md
```

`employee_management.py` is a suggested filename. Replace it with the
actual name of your Python file if it is different.

## 🚀 How to Run

**Requirements** - Python 3.x - A terminal or command prompt - No
third-party Python packages are required

**1. Clone your repository**

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Open the project directory**

``` bash
cd Employee-Management-System
```

**3. Run the program**

``` bash
python employee_management.py
```

If your Python installation uses the `py` launcher on Windows, you can
also run:

``` bash
py employee_management.py
```

## 🧠 Learning Outcomes

By building this project, I practised:

- Creating classes and objects
- Initializing attributes with constructors
- Encapsulation using private attributes
- Writing getter and setter methods
- Implementing inheritance with parent and child classes
- Reusing parent methods with `super()`
- Overriding methods in child classes
- Storing objects in lists
- Using loops and conditional statements for a menu
- Checking inheritance with `issubclass()`

## ⚠️ Current Limitations

- Records are stored in lists in memory and are lost when the program
  exits.
- There are no search, update, or delete menu options.
- Duplicate employee IDs are not checked.
- Invalid integer input can raise an error because input validation is
  limited.
- Getter and setter methods exist, but they are not accessible through a
  menu option.
- The current class name `Devloper` and some menu wording contain
  spelling errors.

## 🔮 Future Improvements

- Add search, update, and delete features.
- Validate age, salary, and employee ID input.
- Prevent duplicate employee IDs.
- Save and load records using JSON or CSV.
- Add database support with SQLite.
- Generate employee and department reports.
- Rename `Devloper` to `Developer` consistently.
- Create a graphical interface.

## 🗺️ Roadmap

- [x] Employee class
- [x] Manager subclass
- [x] Developer subclass (currently named `Devloper`)
- [x] Encapsulation and getter/setter methods
- [x] Method overriding
- [x] Menu-driven record creation
- [x] Display records by role
- [x] Inheritance checking
- [ ] Input validation
- [ ] Search, update, and delete
- [ ] Persistent data storage
- [ ] Database integration
- [ ] Graphical user interface

## 👨‍💻 About the Developer

**Python Developer \| Data Science and AI/ML Learner**

I am learning Python and building practical projects to improve my
programming, problem-solving, and software development skills.

### GitHub

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nandan-mandaliya-05/)

## ⭐ Support

If you find this project useful, consider starring the repository,
sharing feedback, or suggesting improvements.

------------------------------------------------------------------------

<div align="center">

### 🚀 Keep Learning. Keep Building. Keep Growing.

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3500&pause=1000&color=00C2FF&center=true&vCenter=true&width=750&lines=Python+%7C+OOP+%7C+Problem+Solving;Keep+Learning+%7C+Keep+Building" alt="Animated footer" />

**Made with ❤️ and Python**

</div>
