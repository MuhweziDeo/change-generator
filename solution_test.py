import unittest
import solution

class ChangeTestCase(unittest.TestCase):
    def test_return_0_if_list_of_coins_is_0(self):
        self.assertEqual(solution.change(5, []), 0)

    def test_return_1_if_list_of_coins_is_0_and_no_amount(self):
        self.assertEqual(solution.change(None, []), 1)
    
    def test_return_0_if_one_coin_in_list_is_0_and_greater_than_amount(self):
        self.assertEqual(solution.change(1, [3]), 0)  

    def test_return_1_if_one_coin_in_list_is_0_and_greater_than_amount(self):
        self.assertEqual(solution.change(3, [1]), 1)   

    def test_return_1_if_one_coin_in_list_is_equal_to_amount(self):
        self.assertEqual(solution.change(1, [1]), 1)

    def test_return_1_if_no_amount(self):
        self.assertEqual(solution.change(1, [1]), 1)  

    def test_return_number_possible_change_combinations(self):
        self.assertEqual(solution.change(7, [1, 2, 4]), 6)                     

if __name__ == '__main__':
    unittest.main()