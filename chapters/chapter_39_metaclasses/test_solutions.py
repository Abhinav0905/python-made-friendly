"""Tests for Chapter 39."""

import contextlib
import io
import unittest

from . import solutions


class MetaclassTests(unittest.TestCase):
    def test_every_class_is_an_instance_of_type(self):
        self.assertEqual(solutions.q01_class_is_instance_of_type(), (type, True))

    def test_three_argument_type_builds_cat(self):
        cat_class = solutions.q02_build_cat()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = cat_class().meow()
        self.assertEqual(result, "Meow")
        self.assertEqual(output.getvalue(), "Meow\n")

    def test_verbose_metaclass_announces_class(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            first = solutions.q03_make_verbose_class("Robin")
            second = solutions.q03_make_verbose_class("Sparrow")
        self.assertEqual((first.__name__, second.__name__), ("Robin", "Sparrow"))
        self.assertIn("Creating class Robin", output.getvalue())
        self.assertIn("Creating class Sparrow", output.getvalue())

    def test_init_subclass_registry(self):
        self.assertIs(solutions.Shape.registry["CircleShape"], solutions.CircleShape)
        self.assertIs(solutions.Shape.registry["SquareShape"], solutions.SquareShape)

    def test_decorator_registry(self):
        registry = solutions.q05_decorator_registry()
        self.assertIs(registry["Triangle"], solutions.Triangle)
        self.assertIs(registry["DecoratedCircle"], solutions.DecoratedCircle)
        self.assertIs(registry["DecoratedRectangle"], solutions.DecoratedRectangle)

    def test_docstring_metaclass_accepts_and_rejects(self):
        made = solutions.q06_make_documented_class("Good", "A useful class.")
        self.assertEqual(made.__doc__, "A useful class.")
        with self.assertRaises(TypeError):
            solutions.q06_make_documented_class("Bad", "")

    def test_exporter_registry(self):
        exported = solutions.q07_export_examples([1, 2, 3])
        self.assertEqual(exported["csv"], "1,2,3")
        self.assertEqual(exported["json"], "[1, 2, 3]")
        with self.assertRaises(ValueError):
            solutions.Exporter.get("pdf")

    def test_interface_metaclass_rejects_missing_method(self):
        with self.assertRaises(TypeError):
            solutions.EnforceInterface(
                "Incomplete",
                (solutions.Drawable,),
                {"draw": lambda self: None},
            )
        self.assertEqual(solutions.DrawableCircle().draw(), "draw circle")

    def test_diamond_mro(self):
        self.assertEqual(solutions.q09_diamond_mro(), ["D", "B", "C", "A", "object"])

    def test_django_summary_names_core_jobs(self):
        summary = solutions.q10_django_modelbase_summary()
        self.assertIn("declared fields", summary)
        self.assertIn("_meta", summary)
        self.assertIn("application registry", summary)
        self.assertIn("DoesNotExist", summary)
        self.assertIn("class_prepared", summary)


if __name__ == "__main__":
    unittest.main()
