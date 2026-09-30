import sys
import os
import unittest

# Allow Python to import files from the src folder
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from timetable import Timetable
from validators import validate_time, validate_time_range
from clash_detector import find_clashes
from timetable_tools import find_free_slots


class TestTimetable(unittest.TestCase):

    def test_valid_time(self):
        self.assertTrue(validate_time("09:30"))

    def test_invalid_time(self):
        self.assertFalse(validate_time("25:70"))

    def test_valid_time_range(self):
        self.assertTrue(
            validate_time_range("09:00", "10:00")
        )

    def test_invalid_time_range(self):
        self.assertFalse(
            validate_time_range("10:00", "09:00")
        )

    def test_add_class(self):
        timetable = Timetable()

        result = timetable.add_class(
            "Python",
            "Monday",
            "09:00",
            "10:00",
            "A101"
        )

        self.assertTrue(result)
        self.assertEqual(
            len(timetable.get_classes()),
            1
        )

    def test_clash_detection(self):
        timetable = Timetable()

        timetable.add_class(
            "Python",
            "Monday",
            "09:00",
            "10:00",
            "A101"
        )

        timetable.add_class(
            "Physics",
            "Monday",
            "09:30",
            "10:30",
            "A102"
        )

        clashes = find_clashes(
            timetable.get_classes()
        )

        self.assertEqual(len(clashes), 1)

    def test_no_clash(self):
        timetable = Timetable()

        timetable.add_class(
            "Python",
            "Monday",
            "09:00",
            "10:00",
            "A101"
        )

        timetable.add_class(
            "Physics",
            "Monday",
            "10:00",
            "11:00",
            "A102"
        )

        clashes = find_clashes(
            timetable.get_classes()
        )

        self.assertEqual(len(clashes), 0)

    def test_free_slots(self):
        timetable = Timetable()

        timetable.add_class(
            "Python",
            "Monday",
            "09:00",
            "10:00",
            "A101"
        )

        slots = find_free_slots(
            timetable.get_classes(),
            "Monday"
        )

        self.assertIn(
            "08:00 - 09:00",
            slots
        )

        self.assertIn(
            "10:00 - 18:00",
            slots
        )


if __name__ == "__main__":
    unittest.main()
