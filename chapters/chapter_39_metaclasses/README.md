# Metaclasses

## Check Your Understanding

1. **What is a metaclass?** It is the class that creates class objects. Python uses `type` unless a class names another metaclass.
2. **How does `__init_subclass__` differ?** A base class's hook runs when one of its subclasses is made. It is simpler when the behavior belongs to one family of classes; a metaclass is for controlling class creation itself.
3. **What is the method resolution order?** The MRO is the ordered path Python searches for attributes in an inheritance graph. It also determines where `super()` goes next.
4. **Which real library uses one?** Django's ORM uses `ModelBase` to turn field declarations on a model class into metadata used by queries, migrations and related framework code.

## Try It Yourself

1. Confirm that a class is an instance of `type`: `q01_class_is_instance_of_type()`.
2. Build `Cat` with the three-argument form of `type`: `q02_build_cat()`.
3. Announce new classes with `VerboseMeta`: `q03_make_verbose_class()`.
4. Register shape subclasses with `__init_subclass__`: `Shape`.
5. Build an opt-in decorator registry: `register` and `q05_decorator_registry()`.
6. Require class docstrings: `RequireDocstring`.
7. Register exporters by extension: `Exporter` and `q07_export_examples()`.
8. Reject classes that miss required methods: `EnforceInterface`.
9. Inspect a diamond hierarchy: `q09_diamond_mro()`.
10. Summarize Django's model metaclass: `q10_django_modelbase_summary()`.

For Exercise 9, `D(B, C)` has the MRO `D, B, C, A, object`: Python checks the
class itself, follows the left base before the right one, visits their shared
base once and ends at `object`.

The final answer describes Django's design without importing Django, so the
chapter remains standard-library only. It was checked against Django's
[`ModelBase` source](https://github.com/django/django/blob/main/django/db/models/base.py)
and [`_meta` API documentation](https://docs.djangoproject.com/en/5.2/ref/models/meta/)
on August 22, 2026. Framework internals can change between releases.
