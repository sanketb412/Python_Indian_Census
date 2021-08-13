# ''""
# @Author: Sanket Bagde
# @Date: 2021-12-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a Python to check unittest for east test case.
# '''

import unittest
import sys
import os
import csv
from dotenv import load_dotenv
load_dotenv()
sys.path.append(",")

from State_analyser import StateCensusAnalyser
from detect_delimiter import detect


class MyStateTestCase(unittest.TestCase):
    def test_count_number_of_census_rows(self):
        new_count = StateCensusAnalyser(os.getenv("CENSUS_PATH") ,os.getenv("OPERATION"))
        val = new_count.census_count()
        self.assertEqual(val, 29)

    def test_census_file_path(self):
        with self.assertRaises(Exception):
            with open(os.getenv("CENSUS_PATH1"), os.getenv("OPERATION")) as file:
                file_reader = csv.reader(file)
                for rows in file_reader:
                    print(rows)

    def test_census_file_type(self):
        y, file_extension1 = os.path.split(os.getenv("CENSUS_PATH"))    
        extension = file_extension1
        self.assertIn('.csv', extension) 

    def test_census_file_delimiter(self):
        with open( os.getenv("CENSUS_PATH"), 'r') as file:
            reader = csv.reader(file)
            for rows in reader:
                print(rows)
                self.assertEqual(detect(rows), ',')
                    
if __name__ == '__main__':
    unittest.main()