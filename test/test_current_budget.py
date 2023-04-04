import unittest
from src.expense_tracker import Expense


class TestCurrentBudget(unittest.TestCase):
    def test_add_expense(self):

        # Tests if adding the expense makes sense
        E = Expense()
        E.Add_Budget(2000)

        self.assertEqual(E.add_expense(100), 1900)
        # self.assertEqual(E.purchase_prompt(), True)


if __name__ == "__main__":
    # Unit test
    unittest.main()
