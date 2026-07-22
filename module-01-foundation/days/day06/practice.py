from abc import ABC, abstractmethod

# =====================================================================
# 1. Spot the SRP Violation (Refactored)
# =====================================================================
# Old way: One class did everything.
# New way: We split the responsibilities into focused classes.

class Report:
    def __init__(self, content):
        self.content = content

class ReportSaver:
    def save(self, report):
        print(f"Saving report content: '{report.content}' to database.")

class ReportMailer:
    def send(self, report, email):
        print(f"Sending email containing: '{report.content}' to {email}.")


# =====================================================================
# 2. Refactor to OCP (Open/Closed Principle) & 4. Shape Factory
# =====================================================================
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

# 4. Shape Factory
class ShapeFactory:
    @staticmethod
    def create(kind, *args):
        if kind.lower() == "circle":
            return Circle(*args)
        elif kind.lower() == "square":
            return Square(*args)
        elif kind.lower() == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {kind}")


# =====================================================================
# 3. Write a Singleton (AppSettings)
# =====================================================================
class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            # Create the one and only instance
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


# =====================================================================
# 5. Write an Observer Pair
# =====================================================================
class NewsAgency:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self, news):
        for sub in self._subscribers:
            sub.update(news)

class PhoneSubscriber:
    def update(self, news):
        print(f"[Phone Notification] News alert: {news}")

class EmailSubscriber:
    def update(self, news):
        print(f"[Email Notification] News alert: {news}")


# =====================================================================
# TESTING PRACTICE TASKS
# =====================================================================
print("--- 3. Singleton Test ---")
config1 = AppSettings()
config2 = AppSettings()
print(f"Is config1 the same object as config2? {config1 is config2}")  # Must print True

print("\n--- 4. Shape Factory Test ---")
my_circle = ShapeFactory.create("circle", 5)
print(f"Circle Area: {my_circle.area():.2f}")

print("\n--- 5. Observer Test ---")
agency = NewsAgency()
phone = PhoneSubscriber()
email = EmailSubscriber()

agency.subscribe(phone)
agency.subscribe(email)
agency.notify("CodeOps Day 6 lessons are successfully completed!")