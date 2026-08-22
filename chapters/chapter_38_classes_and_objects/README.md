# Classes and Objects

## Check Your Understanding

1. **What is the difference between a class and an object?** A class is a blueprint, such as a description of what every bank account stores and can do. An object is one account built from that blueprint, with its own owner and balance.
2. **When is `__init__` called, and what is it for?** Python calls it automatically after creating an object. It sets the new object's starting instance attributes.
3. **What happens in `rex.bark()`?** Python finds `bark` on Rex's class and calls it as `Dog.bark(rex)`. The object before the dot becomes the method's `self` argument.
4. **Why should a changing list rarely be a class attribute?** A mutable class attribute is shared by every instance. Put `self.items = []` in `__init__` when each object needs a separate list.

## Try It Yourself

1. Implement a circle with `area()` and `grow()`: `q01_make_circle()` and `Circle`.
2. Create two circles and prove that changing one does not change the other: `q02_independent_circles()`.
3. Read the shared value of pi through the class and an instance: `q03_pi_values()`.
4. Transfer money between two accounts: `BankAccount.transfer()`.

The manuscript's Questions & Answers section discusses four different class
questions rather than answering these four exercises. The numbering here
follows the actual Try It Yourself block.

Run the examples:

```bash
python -m chapters.chapter_38_classes_and_objects.solutions
```
