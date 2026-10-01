import unittest
import day2


class TestDay2(unittest.TestCase):
    def test_string_values(self):
        self.assertEqual(day2.text, "Cal Poly")
        self.assertEqual(day2.length, 8)
        self.assertEqual(day2.last_index, 7)
        self.assertEqual(day2.last, "y")
        self.assertEqual(day2.first, "C")


if __name__ == "__main__":
    unittest.main()
