from project.student_report_card import StudentReportCard
import unittest


class SchoolReportCardTests(unittest.TestCase):
    STUDENT_NAME = 'Alex'
    SCHOOL_YEAR = 11

    def setUp(self):
        self.student_report_card = StudentReportCard(self.STUDENT_NAME, self.SCHOOL_YEAR)

    def test__init(self):
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test__student__name_property(self):
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)

        with self.assertRaises(ValueError) as error:
            self.student_report_card.student_name = ''
        self.assertIsNotNone(error.exception)
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)

    def test__student_name_property__invalid_params__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.student_name = ''
        self.assertIsNotNone(error.exception)
        self.assertEqual("Student Name cannot be an empty string!", str(error.exception))

    def test__school_year_property(self):
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)

        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = 0
        self.assertIsNotNone(error.exception)
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)

    def test__school_year_property__params_0__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = 0
        self.assertIsNotNone(error.exception)
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test__school_year_property__params_negative__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = -3
        self.assertIsNotNone(error.exception)
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test__school_year_property__params_too_big__expect_error(self):
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = 13
        self.assertIsNotNone(error.exception)
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test__add_grade__subject_not_in_grades_by_subject(self):
        self.student_report_card.grades_by_subject["Math"] = []
        self.student_report_card.grades_by_subject["Art"] = []
        self.assertEqual({"Math": [], "Art": []}, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade("Biology", 5.23)
        self.student_report_card.add_grade("Biology", 3.89)
        self.assertEqual({"Math": [], "Art": [], "Biology": [5.23, 3.89]}, self.student_report_card.grades_by_subject)

    def test__add_grade__subject_in_grades_by_subject(self):
        self.student_report_card.grades_by_subject["Math"] = [5.34, 3.21, 6]
        self.student_report_card.grades_by_subject["Art"] = []
        self.assertEqual({"Math": [5.34, 3.21, 6], "Art": []}, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade("Math", 5.8)
        self.assertEqual({"Math": [5.34, 3.21, 6, 5.8], "Art": []}, self.student_report_card.grades_by_subject)

        self.student_report_card.add_grade("Art", 6)
        self.student_report_card.add_grade("Art", 4.5)
        self.student_report_card.add_grade("Art", 5.7)
        self.assertEqual({"Math": [5.34, 3.21, 6, 5.8], "Art": [6, 4.5, 5.7]}, self.student_report_card.grades_by_subject)

    def test__add_grade__empty_grades_by_subject(self):
        self.assertEqual({}, self.student_report_card.grades_by_subject)
        self.student_report_card.add_grade("Math", 5.80)
        self.assertEqual({"Math": [5.80]}, self.student_report_card.grades_by_subject)

    def test__average_grade_by_subject__empty_grades_by_subject(self):
        self.assertEqual({}, self.student_report_card.grades_by_subject)
        self.assertEqual('', self.student_report_card.average_grade_by_subject())

    def test__average_grade_by_subject__subject_wth_no_grade__expect_error(self):
        self.student_report_card.grades_by_subject["Math"] = []
        with self.assertRaises(ZeroDivisionError) as error:
            self.student_report_card.average_grade_by_subject()
        self.assertIsNotNone(error.exception)

    def test__average_grade_by_subject(self):
        self.student_report_card.grades_by_subject["Math"] = [3, 4, 5]
        self.student_report_card.grades_by_subject["Art"] = [6, 4, 5]
        result = self.student_report_card.average_grade_by_subject()
        expected_result = f"Math: 4.00\nArt: 5.00"
        self.assertEqual(expected_result, result)

    def test__average_grade_for_all_subjects__empty_grades_by_subject_expect_error(self):
        self.assertEqual({}, self.student_report_card.grades_by_subject)
        with self.assertRaises(ZeroDivisionError) as error:
            self.student_report_card.average_grade_for_all_subjects()
        self.assertIsNotNone(error.exception)

    def test__average_grade_for_all_subjects(self):
        average_grade = (sum([3.4, 5, 6, 4.99]) + sum([2, 5.87, 3, 4.12])) / len([3.4, 5, 6, 4.99]+[2, 5.87, 3, 4.12])
        self.student_report_card.grades_by_subject["Math"] = [3.4, 5, 6, 4.99]
        self.student_report_card.grades_by_subject["Science"] = [2, 5.87, 3, 4.12]
        result = self.student_report_card.average_grade_for_all_subjects()
        expected_result = f"Average Grade: {average_grade:.2f}"
        self.assertEqual(expected_result, result)

    def test__repr__empty_grades_by_subject__expect_error(self):
        with self.assertRaises(ZeroDivisionError) as error:
            self.student_report_card.__repr__()
        self.assertIsNotNone(error.exception)

    def test__repr(self):
        self.student_report_card.grades_by_subject["Math"] = [3.56, 3.67, 6]
        self.student_report_card.grades_by_subject["Art"] = [5, 6, 4.67]
        self.student_report_card.grades_by_subject["Music"] = [5, 6, 6, 5.67]

        result = self.student_report_card.__repr__()
        expected_error = f"Name: {self.student_report_card.student_name}\n" \
                 f"Year: {self.student_report_card.school_year}\n" \
                 f"----------\n" \
                 f"{self.student_report_card.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.student_report_card.average_grade_for_all_subjects()}"
        self.assertEqual(expected_error, result)


if __name__ == '__main__':
    unittest.main()
