# SOLID — the five rules in plain English

Think of SOLID as five habits that stop your code from turning into spaghetti as it grows. Each letter fixes one specific kind of pain.

---

## S — Single Responsibility Principle

**In plain words:** A class should do one thing. One reason to change.

**Bad:**
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_db(self): ...           # database stuff
    def send_welcome_email(self): ...   # email stuff
    def generate_pdf_report(self): ...  # reporting stuff
```
This `User` changes when the DB schema changes, AND when you switch from SMTP to SendGrid, AND when marketing wants a new report layout. Three bosses, one class.

**Good:**
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:   # knows about DB
    def save(self, user): ...

class EmailService:     # knows about email
    def send_welcome(self, user): ...

class UserReport:       # knows about reports
    def generate(self, user): ...
```

**Why it matters:** When marketing changes the report, the DB code isn't at risk.

---

## O — Open/Closed Principle

**In plain words:** Open for **extension**, closed for **modification**. You should be able to add new behavior without editing working code.

**Bad:**
```python
class DiscountCalculator:
    def calculate(self, customer_type, price):
        if customer_type == "regular":
            return price
        elif customer_type == "vip":
            return price * 0.9
        elif customer_type == "employee":
            return price * 0.7
        # Adding "student"? Back to editing this file again.
```
Every new customer type = reopening and risking this class.

**Good:**
```python
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...

class RegularDiscount(DiscountStrategy):
    def apply(self, price): return price

class VipDiscount(DiscountStrategy):
    def apply(self, price): return price * 0.9

class StudentDiscount(DiscountStrategy):   # new file, no edits elsewhere
    def apply(self, price): return price * 0.5
```

**Why it matters:** Old, tested code stays untouched. You only add.

---

## L — Liskov Substitution Principle

**In plain words:** If `B` inherits from `A`, I should be able to use `B` anywhere I use `A` — and nothing should break or surprise me.

**Bad (the classic square/rectangle trap):**
```python
class Rectangle:
    def set_width(self, w): self.w = w
    def set_height(self, h): self.h = h
    def area(self): return self.w * self.h

class Square(Rectangle):
    def set_width(self, w):
        self.w = w
        self.h = w   # sneaky side effect
    def set_height(self, h):
        self.w = h
        self.h = h
```
Now this innocent-looking test fails for `Square`:
```python
def test_rectangle(r: Rectangle):
    r.set_width(5)
    r.set_height(4)
    assert r.area() == 20   # Square returns 16. Broken contract.
```
Mathematically a square *is a* rectangle. In code, it behaves differently — so it's not substitutable.

**Good:** Don't force the inheritance. Give them a common parent `Shape`, or just keep `Square` and `Rectangle` separate. Inheritance is a promise about behavior, not a taxonomy exercise.

---

## I — Interface Segregation Principle

**In plain words:** Don't force a class to implement methods it doesn't need. Many small interfaces beat one fat one.

**Bad:**
```python
class Worker(ABC):
    @abstractmethod
    def work(self): ...
    @abstractmethod
    def eat(self): ...
    @abstractmethod
    def sleep(self): ...

class Robot(Worker):
    def work(self): ...
    def eat(self):   raise NotImplementedError   # 🙃
    def sleep(self): raise NotImplementedError   # 🙃
```

**Good:**
```python
class Workable(ABC):
    @abstractmethod
    def work(self): ...

class Biological(ABC):
    @abstractmethod
    def eat(self): ...
    @abstractmethod
    def sleep(self): ...

class Human(Workable, Biological): ...
class Robot(Workable): ...          # no fake methods
```

**Why it matters:** No more `NotImplementedError` landmines. No more "I only needed `send()` but I had to implement 12 methods."

---

## D — Dependency Inversion Principle

**In plain words:** Depend on **abstractions**, not concrete implementations. High-level code shouldn't be married to a specific low-level library.

**Bad:**
```python
class MySQLDatabase:
    def save(self, data): ...

class OrderService:
    def __init__(self):
        self.db = MySQLDatabase()    # hardcoded
    def place_order(self, order):
        self.db.save(order)
```
Problems: can't swap to Postgres, can't unit-test without a real MySQL, can't reuse `OrderService` elsewhere.

**Good:**
```python
class Database(ABC):
    @abstractmethod
    def save(self, data): ...

class MySQLDatabase(Database): ...
class PostgresDatabase(Database): ...
class InMemoryDatabase(Database): ...   # perfect for tests

class OrderService:
    def __init__(self, db: Database):   # injected
        self.db = db
    def place_order(self, order):
        self.db.save(order)

# Production
service = OrderService(PostgresDatabase())
# Tests
service = OrderService(InMemoryDatabase())
```

**Why it matters:** Testable, swappable, and `OrderService` doesn't care *how* data is saved — only that it *can* be saved.

---

## One-line cheat sheet

- **S** — one class, one job
- **O** — add new code, don't edit old code
- **L** — subclasses must honor the parent's promises
- **I** — many small interfaces > one fat interface
- **D** — depend on interfaces, inject the concrete thing

A useful sanity check when reviewing code: if changing *one* requirement forces you to edit *five* files that seem unrelated — some SOLID principle is probably being violated.