"""Worked exercises for Chapter 38: Classes and Objects."""


class Circle:
    """A circle whose radius can grow independently of other circles."""

    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return this circle's area."""
        return self.pi * self.radius ** 2

    def grow(self):
        """Double this circle's radius and return the new radius."""
        self.radius *= 2
        return self.radius


def q01_make_circle(radius):
    """Exercise 1: build and return a Circle."""
    return Circle(radius)


def q02_independent_circles(first_radius, second_radius):
    """Exercise 2: grow one circle and return both resulting radii."""
    first = Circle(first_radius)
    second = Circle(second_radius)
    first.grow()
    return first.radius, second.radius


def q03_pi_values(radius=1):
    """Exercise 3: read pi through both the class and an instance."""
    circle = Circle(radius)
    return Circle.pi, circle.pi


class BankAccount:
    """A small account used to demonstrate methods that change state."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("deposit amount cannot be negative")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("withdrawal amount cannot be negative")
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, amount, other_account):
        """Exercise 4: move funds only when this account can cover them."""
        if not isinstance(other_account, BankAccount):
            raise TypeError("other_account must be a BankAccount")
        if not self.withdraw(amount):
            return False
        other_account.deposit(amount)
        return True


def main():
    small = q01_make_circle(2)
    print(f"Circle area: {small.area():.5f}")
    print("Independent radii:", q02_independent_circles(2, 5))

    checking = BankAccount("Asha", 100)
    savings = BankAccount("Asha", 25)
    checking.transfer(40, savings)
    print("Balances after transfer:", checking.balance, savings.balance)


if __name__ == "__main__":
    main()
