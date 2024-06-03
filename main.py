from person import Person
from employee import Employee
from safe_employee import SaleEmployee

# Python Inheritance

## Introduction to the Python inheritance

employee = Employee("John", "Python Developer")
print(employee.greet())

## Inheritance terminology

## type vs. isinstance

person = Person("Jahe")
print(type(person))   # <class person.Person>

employee = Employee("John", "Python Developer")
print(type(employee)) # <class employee.Employee>

print(isinstance(person, Person))     # True
print(isinstance(employee, Person))   # True
print(isinstance(employee, Employee)) # True
print(isinstance(person, Employee))   # False

## issubclass

print(issubclass(Employee, Person))       # True
print(issubclass(SaleEmployee, Employee)) # True
print(issubclass(SaleEmployee, Person))   # True

print(issubclass(Person, object))         # True
