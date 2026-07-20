import math

# =========================================================
# EXERCISE 1: Spot the SRP (Single Responsibility) Violation
# =========================================================
# Split a Report class (which had data, saving, and emailing) into 3 focused classes.

class Report:
    """Class responsible ONLY for holding and building report data."""
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_formatted_report(self):
        return f"=== {self.title} ===\n{self.content}"


class ReportSaver:
    """Class responsible ONLY for saving a report to disk."""
    def save_to_file(self, report, filename):
        print(f"[Saver] Saving report '{report.title}' to {filename}...")


class ReportEmailer:
    """Class responsible ONLY for emailing a report."""
    def email_report(self, report, recipient):
        print(f"[Emailer] Sending report '{report.title}' to {recipient}...")


# =========================================================
# EXERCISE 2 & 4: Open/Closed Principle (OCP) & Factory Pattern
# =========================================================
# Refactored shapes to inherit from a base Shape class (OCP).
# Created a ShapeFactory to handle instantiation (Factory Pattern).

class Shape:
    """Base class. Open for extension, closed for modification."""
    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class ShapeFactory:
    """Factory to create shapes dynamically without exposing construction logic."""
    @staticmethod
    def create(kind, *args):
        kind = kind.lower()
        if kind == "circle":
            return Circle(*args)
        elif kind == "square":
            return Square(*args)
        elif kind == "triangle":
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {kind}")


# =========================================================
# EXERCISE 3: Singleton Pattern
# =========================================================
# Holds configuration details where only ONE instance is ever created.

class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


# =========================================================
# EXERCISE 5: Observer Pattern Pair
# =========================================================
# A Subject (NewsAgency) that notifies registered observers when news updates.

class NewsAgency:
    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def notify(self):
        for sub in self._subscribers:
            sub.update(self._latest_news)

    def publish_news(self, news):
        self._latest_news = news
        print(f"\n[Agency] Publishing news: '{news}'")
        self.notify()


class NewsSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"[{self.name}] Received update: {news}")


# =========================================================
# TEST DRIVER (Verification)
# =========================================================
if __name__ == "__main__":
    print("--- Testing Exercise 1 (SRP) ---")
    rep = Report("Monthly Audit", "All finances are stable.")
    saver = ReportSaver()
    emailer = ReportEmailer()
    saver.save_to_file(rep, "audit.txt")
    emailer.email_report(rep, "manager@company.com")

    print("\n--- Testing Exercise 2 & 4 (OCP & Factory) ---")
    c = ShapeFactory.create("circle", 5)
    s = ShapeFactory.create("square", 4)
    t = ShapeFactory.create("triangle", 6, 3)
    print(f"Circle Area: {c.area():.2f}")
    print(f"Square Area: {s.area():.2f}")
    print(f"Triangle Area: {t.area():.2f}")

    print("\n--- Testing Exercise 3 (Singleton) ---")
    config1 = AppSettings()
    config2 = AppSettings()
    print(f"Config 1 Currency: {config1.currency}")
    print(f"Are both configurations the same instance? {config1 is config2}")

    print("\n--- Testing Exercise 5 (Observer) ---")
    agency = NewsAgency()
    user1 = NewsSubscriber("Abebe")
    user2 = NewsSubscriber("Aster")
    agency.subscribe(user1)
    agency.subscribe(user2)
    agency.publish_news("CodeOps Day 6 Assignments Completed!")