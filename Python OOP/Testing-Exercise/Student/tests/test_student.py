import unittest
from unittest import TestCase
from project.student import Student


class StudentTest(TestCase):
    NAME = "Jasmine"
    COURSES = {"Computer science": ["some", "notes"], "Math": ["some", "more", "notes"]}

    def setUp(self):
        self.student = Student(self.NAME, self.COURSES)

    def test__init__courses(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual(self.COURSES, self.student.courses)

    def test__init__courses_equal_to_none(self):
        student = Student(self.NAME, None)
        self.assertEqual(self.NAME, student.name)
        self.assertEqual({}, student.courses)

    def test__enroll__already_added(self):
        result = self.student.enroll("Computer science", ["more", "notes"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test__enroll__course_n_notes_added(self):
        result = self.student.enroll("French", ["more", "notes"], "Y")
        self.assertEqual("Course and course notes have been added.", result)

    def test__enroll__course_added(self):
        result = self.student.enroll("Spanish", ["more", "notes"], "N")
        self.assertEqual("Course has been added.", result)

    def test__add_notes__valid(self):
        result = self.student.add_notes("Computer science", ["hi"])
        self.assertEqual("Notes have been updated", result)

    def test__add_notes__invalid(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Art", ["panting"])
        self.assertIsNotNone(ex)

    def test__leave_course__valid(self):
        result = self.student.leave_course("Math")
        self.assertEqual("Course has been removed", result)

    def test__leave_course__invalid(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Art")
        self.assertIsNotNone(ex)


if __name__ == "__main__":
    unittest.main()
