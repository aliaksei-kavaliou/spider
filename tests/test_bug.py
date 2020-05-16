import unittest
from unittest.mock import patch
from io import StringIO
import sys
import bug

class TestBug(unittest.TestCase):
    def test_load_file(self):
        expected = [
            ["|", " ", "|", ],
            ["#", "#", "#", "O", ],
            ["|", " ", "|", ],
        ]
        result = bug.load_file("tests/data/bug.txt")
        self.assertEqual(expected, result)

    @patch('builtins.input', lambda x: 'tests/data/bug.txt' if x == 'Load bug file: ' else 'tests/data/landscape.txt' )
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        bug.main()
        self.assertEqual('Found 3 bugs.', mock_stdout.getvalue().strip("\n")) 
    

if __name__ == "__main__":
    unittest.main()
