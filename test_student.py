import unittest
from student import calculate_grade

class TestStudentGrade(unittest.TestCase):

    def test_grade_s(self):
        self.assertEqual(calculate_grade(95), "S")

    def test_grade_a(self):
        self.assertEqual(calculate_grade(85), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(70), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(55), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(45), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(30), "F")

    def test_boundary_values(self):
        self.assertEqual(calculate_grade(90), "S")
        self.assertEqual(calculate_grade(80), "A")
        self.assertEqual(calculate_grade(65), "B")
        self.assertEqual(calculate_grade(50), "C")
        self.assertEqual(calculate_grade(40), "D")

if __name__ == "__main__":
    unittest.main()
