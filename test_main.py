import unittest
from unittest.mock import patch
from main import example_algorithms, main

class TestMain(unittest.TestCase):
    @patch('builtins.print')
    def test_example_algorithms(self, mock_print):
        # Call the function which prints to stdout
        example_algorithms()
        
        # Verify that print was indeed called to prove execution
        self.assertTrue(mock_print.called)
        # Specifically check if the test header was printed
        mock_print.assert_any_call("--- Testing Algorithms ---")

    @patch('main.example_algorithms')
    def test_main(self, mock_example_algorithms):
        # Call the entrypoint method
        main()
        
        # Verify it delegated to the example code
        mock_example_algorithms.assert_called_once()

if __name__ == '__main__':
    unittest.main()
