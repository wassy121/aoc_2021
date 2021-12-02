import sys
import os
sys.path.insert(0, os.path.abspath('../src'))

import unittest
from unittest.mock import patch, mock_open

class testDepths(unittest.TestCase):
    def test_file_is_valid(self):
        with open('src/resources/input.txt') as input_file:
            lines = input_file.readlines()
            length_of_file = len(lines)
            # hardcode
            assert 2000 == length_of_file, "should be 2000 - $(wc -l input.txt)"


    @patch('builtins.open', new_callable=mock_open, read_data='foo')
    def test_parse_file(self, file_handler):
        pass

    def test_increasing_depth(self):
        pass

    def test_decreasing_depth(self):
        pass

if __name__ == '__main__':
    unittest.main()
