# Shape Hierarchy
from math import pi

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses should implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c
    
# 2 Bank Account System
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, value):
        if value <= 0:
            return False
        self.balance += value
        return True

    def withdrawal(self, value):
        if value > self.balance:
            return None
        self.balance -= value
        return self.balance

    def interest(self, rate):
        if rate < 0:
            return None
        return self.balance * rate

class SavingsAccount(Account):
    pass

class CheckingAccount(Account):
    pass

# 3 Vehicle Hierarchy
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def mileage(self, average_yearly_distance):
        current_year = 2024
        return (current_year - self.year) * average_yearly_distance

    def towing_capacity(self):
        raise NotImplementedError("Subclasses should implement this method")

class Car(Vehicle):
    def towing_capacity(self):
        return 1000

class Motorcycle(Vehicle):
    def towing_capacity(self):
        return 0

class Truck(Vehicle):
    def towing_capacity(self):
        return 4000
    
# 4 Employee Hierarchy

class Employee:
    def __init__(self, name, salary, id):
        self.name = name
        self.salary = salary
        self.id = id

class Manager(Employee):
    def __init__(self, name, salary, id):
        super().__init__(name, salary, id)
        self.list_of_employees = set()
        self.meetings = {}

    def add_employee(self, employee):
        self.list_of_employees.add(employee)

    def plan_meeting(self, day_of_the_week, hour):
        if day_of_the_week not in self.meetings:
            self.meetings[day_of_the_week] = []
        self.meetings[day_of_the_week].append(hour)

    def check_meetings(self, day_of_the_week, hour=0):
        if day_of_the_week in self.meetings:
            return [h for h in self.meetings[day_of_the_week] if h >= hour]
        return []

class Engineer(Employee):
    def __init__(self, name, salary, id):
        super().__init__(name, salary, id)
        self.active_projects = []
        self.deactive_projects = []

    def add_project(self, project_name, short_description):
        self.active_projects.append((project_name, short_description))

    def remove_project(self, project_name):
        self.active_projects = [p for p in self.active_projects if p[0] != project_name]

class Salesperson(Employee):
    def __init__(self, name, salary, id):
        super().__init__(name, salary, id)
        self.list_of_products = []

    def add_product(self, product_name, short_description, price):
        self.list_of_products.append((product_name, short_description, price))

    def sell_product(self, product_name):
        self.list_of_products = [p for p in self.list_of_products if p[0] != product_name]

# 5 Animal Hierarchy
class Animal:
    def breed(self):
        raise NotImplementedError("Subclasses should implement this method")

    def eat(self):
        raise NotImplementedError("Subclasses should implement this method")

    def die(self):
        raise NotImplementedError("Subclasses should implement this method")

class Mammal(Animal):
    def walk(self):
        raise NotImplementedError("Subclasses should implement this method")

    def run(self):
        raise NotImplementedError("Subclasses should implement this method")

class Bird(Animal):
    def fly(self):
        raise NotImplementedError("Subclasses should implement this method")

class Fish(Animal):
    def swim(self):
        raise NotImplementedError("Subclasses should implement this method")

# 6 Library Catalog System 
class LibraryItem:
    def __init__(self, id):
        self.id = id
        self.checked_out = False

    def checkout(self):
        if self.checked_out:
            return False
        self.checked_out = True
        return True

    def return_to_library(self):
        if not self.checked_out:
            return False
        self.checked_out = False
        return True

    def display_info(self):
        raise NotImplementedError("Subclasses should implement this method")

class Book(LibraryItem):
    def __init__(self, id, title):
        super().__init__(id)
        self.title = title

    def display_info(self):
        return f"Book: {self.title}"

class DVD(LibraryItem):
    def __init__(self, id, title):
        super().__init__(id)
        self.title = title

    def display_info(self):
        return f"DVD: {self.title}"

class Magazine(LibraryItem):
    def __init__(self, id, title):
        super().__init__(id)
        self.title = title

    def display_info(self):
        return f"Magazine: {self.title}"
    
############
def main():
    # Test Shape Hierarchy
    print("Testing Shape Hierarchy:")
    circle = Circle(5)
    rectangle = Rectangle(10, 20)
    triangle = Triangle(3, 4, 5)

    print(f"Circle area: {circle.area()}, perimeter: {circle.perimeter()}")
    print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")
    print(f"Triangle area: {triangle.area()}, perimeter: {triangle.perimeter()}")

    # Test Bank Account System
    print("\nTesting Bank Account System:")
    savings = SavingsAccount(100)
    checking = CheckingAccount(200)

    print(f"Savings deposit 50: {savings.deposit(50)}, balance: {savings.balance}")
    print(f"Savings withdrawal 30: {savings.withdrawal(30)}, balance: {savings.balance}")
    print(f"Savings interest at 5%: {savings.interest(0.05)}, balance: {savings.balance}")

    print(f"Checking deposit 100: {checking.deposit(100)}, balance: {checking.balance}")
    print(f"Checking withdrawal 150: {checking.withdrawal(150)}, balance: {checking.balance}")
    print(f"Checking interest at 3%: {checking.interest(0.03)}, balance: {checking.balance}")

    # Test Vehicle Hierarchy
    print("\nTesting Vehicle Hierarchy:")
    car = Car("Toyota", "Auris", 2020)
    motorcycle = Motorcycle("Yamaha", "R1", 2018)
    truck = Truck("Ford", "F-150", 2015)

    print(f"Car mileage: {car.mileage(10000)}, towing capacity: {car.towing_capacity()}")
    print(f"Motorcycle mileage: {motorcycle.mileage(5000)}, towing capacity: {motorcycle.towing_capacity()}")
    print(f"Truck mileage: {truck.mileage(15000)}, towing capacity: {truck.towing_capacity()}")

    # Test Employee Hierarchy
    print("\nTesting Employee Hierarchy:")
    manager = Manager("Alice", 90000, 1)
    engineer = Engineer("Bob", 80000, 2)
    salesperson = Salesperson("Charlie", 70000, 3)

    manager.add_employee(engineer)
    manager.add_employee(salesperson)
    manager.plan_meeting("Monday", 10)
    manager.plan_meeting("Monday", 14)

    engineer.add_project("Project X", "Top secret project")
    engineer.add_project("Project Y", "Another secret project")
    engineer.remove_project("Project X")

    salesperson.add_product("Product A", "Description A", 100)
    salesperson.add_product("Product B", "Description B", 200)
    salesperson.sell_product("Product A")

    print(f"Manager's employees: {[e.name for e in manager.list_of_employees]}")
    print(f"Manager's meetings on Monday: {manager.check_meetings('Monday')}")
    print(f"Engineer's active projects: {engineer.active_projects}")
    print(f"Salesperson's products: {salesperson.list_of_products}")

    # Test Animal Hierarchy
    print("\nTesting Animal Hierarchy:")
    mammal = Mammal()
    bird = Bird()
    fish = Fish()

    # These methods are not implemented, so they will raise NotImplementedError
    try:
        mammal.walk()
    except NotImplementedError:
        print("Mammal walk method not implemented")

    try:
        bird.fly()
    except NotImplementedError:
        print("Bird fly method not implemented")

    try:
        fish.swim()
    except NotImplementedError:
        print("Fish swim method not implemented")

    # Test Library Catalog System
    print("\nTesting Library Catalog System:")
    book = Book(1, "Alice in Wonderland")
    dvd = DVD(2, "Inception")
    magazine = Magazine(3, "National Geographic")

    print(f"Book info: {book.display_info()}")
    print(f"DVD info: {dvd.display_info()}")
    print(f"Magazine info: {magazine.display_info()}")

    print(f"Book checkout: {book.checkout()}")
    print(f"Book return: {book.return_to_library()}")
    print(f"Book return again: {book.return_to_library()}")

if __name__ == "__main__":
    main()