# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
"""Unit tests for the StrOptions class."""
import unittest
from typing import Any

from pss3000.commands.common import StrOptions


class TestStrOptions(unittest.TestCase):
    def test_constructor_without_args(self) -> None:
        def construct_stroptions_without_args() -> None:
            _str_options = StrOptions()

        self.assertRaises(ValueError, construct_stroptions_without_args)

    def test_constructor_without_default(self) -> None:
        str_options = StrOptions("Option one", "Option two", "Option three")

        self.assertEqual(str_options.default, "Option one")

        def get_item(obj: Any, index: int) -> Any:
            return obj[index]

        self.assertEqual(len(str_options), 3)
        self.assertEqual(str_options[0], "Option one")
        self.assertEqual(str_options[1], "Option two")
        self.assertEqual(str_options[2], "Option three")
        self.assertRaises(IndexError, get_item, str_options, 3)

        options = list(str_options)
        self.assertEqual(len(options), 3)
        self.assertEqual(options[0], "Option one")
        self.assertEqual(options[1], "Option two")
        self.assertEqual(options[2], "Option three")
        self.assertRaises(IndexError, get_item, options, 3)

    def test_constructor_with_default(self) -> None:
        str_options = StrOptions(
            "Option one", "Option two", "Option three", default="Option three"
        )

        self.assertEqual(str_options.default, "Option three")

        def get_item(obj: Any, index: int) -> Any:
            return obj[index]

        self.assertEqual(len(str_options), 3)
        self.assertEqual(str_options[0], "Option one")
        self.assertEqual(str_options[1], "Option two")
        self.assertEqual(str_options[2], "Option three")
        self.assertRaises(IndexError, get_item, str_options, 3)

        options = list(str_options)
        self.assertEqual(len(options), 3)
        self.assertEqual(options[0], "Option one")
        self.assertEqual(options[1], "Option two")
        self.assertEqual(options[2], "Option three")
        self.assertRaises(IndexError, get_item, options, 3)

    def test_constructor_with_invalid_default(self) -> None:
        def construct_with_invalid_default() -> None:
            _str_options = StrOptions(
                "Option one",
                "Option two",
                "Option three",
                default="Option four",
            )

        self.assertRaises(ValueError, construct_with_invalid_default)

    def test_getattr(self) -> None:
        str_options = StrOptions("Option one", "Option two", "Option three")
        self.assertEqual(str_options.option_one, "Option one")
        self.assertEqual(str_options.option_two, "Option two")
        self.assertEqual(str_options.option_three, "Option three")

    def test_getattr_wrong_case(self) -> None:
        def get_invalid_attr() -> None:
            str_options = StrOptions("Option one", "Option two", "Option three")
            _x = str_options.Option_one

        self.assertRaises(IndexError, get_invalid_attr)

    def test_getattr_nonexistent(self) -> None:
        def get_invalid_attr() -> None:
            str_options = StrOptions("Option one", "Option two", "Option three")
            _x = str_options.option_four

        self.assertRaises(IndexError, get_invalid_attr)

    def test_option_with_non_alphanumeric_chars(self) -> None:
        str_options = StrOptions("I'm_just.   Testing-things.out.   Success?")

        self.assertEqual(
            str_options.im_just_testing_things_out_success,
            "I'm_just.   Testing-things.out.   Success?",
        )
