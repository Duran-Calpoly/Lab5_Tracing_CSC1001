import unittest
import day1


class TestDay1(unittest.TestCase):
    def test_task1_list_values(self):
        self.assertEqual(day1.values, [4, 5, 6, 7])
        self.assertEqual(day1.first, 4)
        self.assertEqual(day1.second, 5)
        self.assertEqual(day1.last, 7)
        self.assertTrue(day1.comparison)

    def test_task2_index_expression(self):
        self.assertEqual(day1.letters, ["a", "b", "c", "d", "e", "f"])
        self.assertEqual(day1.index, 4)
        self.assertEqual(day1.letter, "e")
        self.assertEqual(day1.direct, "e")


if __name__ == "__main__":
    unittest.main()
