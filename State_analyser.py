# ''""
# @Author: Sanket Bagde
# @Date: 2021-11-08
# @Last Modified by:
# @Last Modified time:
# @Title :Write a program to read csv file.
# '''

import csv
import os
from dotenv import load_dotenv
load_dotenv()
print("Welcome to Indian State Census Analyser")

class StateCensusAnalyser:
    def __init__(self, path, operation):
        self.path = path
        self.operation = operation

    def census_file(self):
        print("\tState Census Data:-")
        try:
            with open( self.path, self.operation) as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)                    
        except:
            print("Something went Wrong. File path is not correct..!!")
        finally:
            file.close()

    def census_count(self):
        try:
            with open(self.path, self.operation) as file:
                reader = csv.reader(file)

                data = list(reader)
                row_count = len(data)
                return row_count - 1
        except:
            print("Something went Wrong. File path is not correct..!!")
        finally:
            file.close()

if __name__ == '__main__':
    census_obj = StateCensusAnalyser(os.getenv('CENSUS_PATH'), os.getenv('OPERATION'))
    census_obj.census_file()

   