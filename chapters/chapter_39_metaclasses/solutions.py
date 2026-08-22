"""Worked exercises for Chapter 39: Metaclasses."""

import json


class Dog:
    pass


def q01_class_is_instance_of_type():
    """Exercise 1: prove that Dog is an instance of type."""
    return type(Dog), isinstance(Dog, type)


def _meow(self):
    print("Meow")
    return "Meow"


def q02_build_cat():
    """Exercise 2: construct a class without the class keyword."""
    return type("Cat", (), {"meow": _meow})


class VerboseMeta(type):
    """A metaclass that announces each class it creates."""

    def __new__(mcls, name, bases, namespace):
        print(f"Creating class {name}")
        return super().__new__(mcls, name, bases, namespace)


def q03_make_verbose_class(name):
    """Exercise 3: create a named class through VerboseMeta."""
    return VerboseMeta(name, (), {})


class Shape:
    """Exercise 4: register every concrete shape as it is defined."""

    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Shape.registry[cls.__name__] = cls


class CircleShape(Shape):
    pass


class SquareShape(Shape):
    pass


_decorator_registry = {}


def register(cls):
    """Exercise 5: opt a class into a registry with a decorator."""
    _decorator_registry[cls.__name__] = cls
    return cls


@register
class Triangle:
    pass


@register
class DecoratedCircle:
    def area(self):
        return 3.14159 * self.radius ** 2


@register
class DecoratedRectangle:
    def area(self):
        return self.width * self.height


def q05_decorator_registry():
    return dict(_decorator_registry)


class RequireDocstring(type):
    """Exercise 6: reject a class whose body has no docstring."""

    def __new__(mcls, name, bases, namespace):
        docstring = namespace.get("__doc__")
        if docstring is None or not docstring.strip():
            raise TypeError(f"Class {name!r} needs a docstring")
        return super().__new__(mcls, name, bases, namespace)


def q06_make_documented_class(name, docstring):
    namespace = {"__doc__": docstring}
    return RequireDocstring(name, (), namespace)


class Exporter:
    """Exercise 7: map file extensions to exporter subclasses."""

    registry = {}
    extension = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not cls.extension:
            raise TypeError(f"{cls.__name__} must define extension")
        Exporter.registry[cls.extension] = cls

    @classmethod
    def get(cls, extension):
        try:
            exporter_class = cls.registry[extension.lower().lstrip(".")]
        except KeyError as error:
            raise ValueError(f"no exporter for {extension!r}") from error
        return exporter_class()


class CSVExporter(Exporter):
    extension = "csv"

    def export(self, values):
        return ",".join(str(value) for value in values)


class JSONExporter(Exporter):
    extension = "json"

    def export(self, values):
        return json.dumps(values)


def q07_export_examples(values):
    return {
        "csv": Exporter.get("csv").export(values),
        "json": Exporter.get("json").export(values),
    }


class EnforceInterface(type):
    """Exercise 8: require subclass methods at definition time."""

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if bases:
            required = getattr(cls, "required_methods", ())
            missing = [method for method in required if not callable(getattr(cls, method, None))]
            if missing:
                names = ", ".join(missing)
                raise TypeError(f"{name} must define: {names}")
        return cls


class Drawable(metaclass=EnforceInterface):
    required_methods = ("draw", "erase")


class DrawableCircle(Drawable):
    def draw(self):
        return "draw circle"

    def erase(self):
        return "erase circle"


class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


def q09_diamond_mro():
    """Exercise 9: return the class names in D's MRO."""
    return [item.__name__ for item in D.__mro__]


def q10_django_modelbase_summary():
    """Exercise 10: summarize the main class-creation work of ModelBase."""
    return (
        "Django's ModelBase.__new__ separates attributes that implement "
        "contribute_to_class from ordinary class attributes, then creates the "
        "class and its _meta Options object. It installs declared fields and "
        "managers, creates model-specific DoesNotExist, MultipleObjectsReturned "
        "and NotUpdated exceptions, and checks proxy, abstract and multi-table "
        "inheritance. It copies inherited fields and indexes where required, "
        "prepares the finished class, registers non-abstract models with the "
        "application registry and sends Django's class_prepared signal."
    )


def main():
    cat_class = q02_build_cat()
    cat_class().meow()
    print("Shape registry:", sorted(Shape.registry))
    print("Diamond MRO:", q09_diamond_mro())


if __name__ == "__main__":
    main()
