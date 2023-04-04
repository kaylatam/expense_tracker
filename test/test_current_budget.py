import unittest
from src.expense_tracker import Expense


class TestCurrentBudget(unittest.TestCase):
    def test_add_expense(self):

        # Tests if adding the expense makes sense
        E = Expense()
        E.Add_Budget(2000)

        self.assertEqual(E.add_expense(100), 1900)


if __name__ == "__main__":
    # Unit test
    unittest.main()
