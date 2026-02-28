import unittest
from unittest.mock import patch
import demo_bad_code

class TestGetUserData(unittest.TestCase):
    """
    Unit tests for the get_user_data function.
    """

    def setUp(self):
        """
        Set up mock user data for testing.
        """
        self.users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]

    def test_get_user_data_found(self):
        """
        Verifies that a user is correctly found when the ID exists in the list.
        """
        user = demo_bad_code.get_user_data(self.users, 1)
        self.assertIsNotNone(user, "User should be found")
        self.assertEqual(user['name'], 'Alice', "Incorrect user name retrieved")

    def test_get_user_data_not_found(self):
        """
        Verifies that the function returns None when the ID does not exist in the list.
        """
        user = demo_bad_code.get_user_data(self.users, 99)
        self.assertIsNone(user, "User should not be found")

    def test_get_user_data_empty_list(self):
        """
        Verifies behavior when the provided user list is empty.
        """
        user = demo_bad_code.get_user_data([], 1)
        self.assertIsNone(user, "User should be None for an empty list")

class TestProcessPayments(unittest.TestCase):
    """
    Unit tests for the process_payments function.
    """

    @patch('demo_bad_code.time.sleep')
    def test_process_payments_success(self, mock_sleep):
        """
        Verifies the total calculation (price + 10% tax) for a valid list of items.
        Mocks time.sleep to avoid slowing down the tests.
        """
        items = [{'price': 10}, {'price': 20}]
        # Item 1: 10 + 10 * 0.1 = 11
        # Item 2: 20 + 20 * 0.1 = 22
        # Total: 33
        total = demo_bad_code.process_payments(items)
        self.assertEqual(total, 33.0, "Total payment calculated incorrectly")
        
        # Ensure sleep was called for each item
        self.assertEqual(mock_sleep.call_count, 2, "time.sleep should be called once per item")

    @patch('demo_bad_code.time.sleep')
    def test_process_payments_empty_list(self, mock_sleep):
        """
        Verifies that an empty list of items returns a total of 0.
        """
        total = demo_bad_code.process_payments([])
        self.assertEqual(total, 0, "Total should be 0 for empty item list")
        mock_sleep.assert_not_called()

class TestRunBatch(unittest.TestCase):
    """
    Unit tests for the run_batch function.
    """

    def test_run_batch_execution(self):
        """
        Tests the execution of run_batch. 
        Note: The current implementation has a bug where it looks for user ID 3, 
        which doesn't exist, and attempts to access 'name' on a None object.
        This test expects a TypeError to be raised due to this bug.
        """
        with self.assertRaises(TypeError):
            demo_bad_code.run_batch()

if __name__ == '__main__':
    unittest.main()
