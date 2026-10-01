import unittest
import day_3


class TestDay3(unittest.TestCase):
    def test_checked_access_valid_index(self):
        values = [1, 0, 1]
        self.assertEqual(day_3.checked_access(values, 2), 1)
        self.assertEqual(values, [1, 0, 1])

    def test_checked_access_invalid_index(self):
        values = [1, 0, 1]
        self.assertIsNone(day_3.checked_access(values, 9))
        self.assertEqual(values, [1, 0, 1])

    def test_task5_aliases(self):
        self.assertEqual(day_3.first, [10, 20, 30])
        self.assertIs(day_3.first, day_3.second)
        self.assertIs(day_3.second, day_3.third)

    def test_task6_equal_values_and_identity(self):
        self.assertEqual(day_3.a, day_3.c)
        self.assertIs(day_3.a, day_3.b)
        self.assertIs(day_3.c, day_3.d)
        self.assertIsNot(day_3.a, day_3.c)
        self.assertTrue(day_3.same_values)
        self.assertTrue(day_3.same_ab)
        self.assertFalse(day_3.same_ac)

    def test_first_value(self):
        values = [7, 4, 9]
        self.assertEqual(day_3.first_value(values), 7)
        self.assertEqual(values, [7, 4, 9])


if __name__ == "__main__":
    unittest.main()
