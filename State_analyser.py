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
import json

class StateCensusAnalyser:
    """
    A class to represent a StateCensusAnalyser.
    ...
    Attributes
    ----------
    its not taking any attributes
    ...
    Methods
    -------
    census_count(self):
        reading the census.csv file.
    """
    def census_count(self):
        """
            Description:
                function census_count read the csv file
            Parameter:
                reading csv file using csv.reader which is called from enviormrnt folder
            Return:
                returning the count of row to test file.
        """
        try:
            with open(os.getenv("CENSUS_PATH"), os.getenv("OPERATION")) as file:
                reader = csv.reader(file)
                data = list(reader)
                row_count = len(data)
                return row_count - 1
        except:
            print("Something went Wrong. File path is not correct..!!")
        finally:
            print("File Exicuted")

class CSVStates:
    """
    A class to represent a CSVState.
    ...
    Attributes
    ----------
    its not taking any attributes
    ...
    Methods
    -------
    code_count(self):
        reading the census.csv file.
    """    
    def code_count(self):
        """
            Description:
                function code_count read the csv file
            Parameter:
                reading csv file using csv.reader which is called from enviormrnt folder
            Return:
                returning the count of row to test file.
        """        
        try:
            with open(os.getenv("CODE_PATH"), os.getenv("OPERATION")) as file:
                reader = csv.reader(file)
                data = list(reader)
                row_count = len(data)
                return row_count - 1
        except:
            print("Something went Wrong. File path is not correct..!!")
        finally:
            print("File Exicuted")

class StateCensusData(StateCensusAnalyser, CSVStates):
    """
    A class to represent a StateCensusData.
    ...
    Attributes
    ----------
    StateCensusAnalyser : csv data
        csv data from census of state of csv file
    CSVStates : csv data
        csv data from code of state of csv file
    ...
    Methods
    -------
    count(self):
        reading the census.csv file.
    code(self)
        reading the code.csv file.
    """    
    def census(self):
        """
            Description:
                function census read the csv file
            Parameter:
                getting the value from census_count and code_count function and printing both the data from csv file
        """        
        try:
            census_obj = StateCensusAnalyser(os.getenv("CENSUS_PATH"), os.getenv("OPERATION"))
            census_obj.census_file()
            print(census_obj.census_count())
        except Exception:
            print(Exception)

    def code(self):
        try:
            code_obj = CSVStates(os.getenv("CODE_PATH"), os.getenv("OPERATION"))
            code_obj.code_file()
            print(code_obj.code_count())
        except Exception:
            print(Exception)

class Dictionary:
    """
    A class to represent a Dictionary.
    ...
    Attributes
    ----------
    It does not take any attrributes
    ...
    Methods
    -------
    dictionary_data(self):
        to get both of the csv data and put it into dictionary. also creat new file and appent dictionary into it.
    make_json(self)
        convering csv file to json file
    """        
    def dictionary_data(self):
        """
            Description:
                function dictionary_data gets the data from both the csv file and merge the state code of state_code.csv file with census file
            Parameter:
                #declaring globar variable to store census.csv file data
                    census_data=[]
                    code_data=[]
                i, j reading the row from the csv file  
                csv.DictReader to read the file from dictionary
                csv.DictWriter to write the file into new dictionary.  
        """        
        census_data=[]
        code_data=[]
        with open(os.getenv('CENSUS_PATH'), 'r') as data:
            for line in csv.DictReader(data):
                census_data.append(line)

        with open(os.getenv('CODE_PATH'), 'r') as data:
            for line in csv.DictReader(data):
                code_data.append(line)

        for i in range(len(census_data)):
            for j in range(len(code_data)):
                if census_data[i]['State'] == code_data[j]['StateName']:
                    census_data[i]['StateCode'] = code_data[j]['StateCode']
                    break
                else:
                    continue
        
        with open(os.getenv('NEW_CODE_CENSUS_PATH'), 'w', newline="") as csv_new_file:
            fieldnames = list(census_data[0].keys())
            csv_writer = csv.DictWriter(csv_new_file, fieldnames=fieldnames, delimiter=',')
            csv_writer.writeheader()
            for line in census_data:
                csv_writer.writerow(line)
        

    def make_json(self, csvFilePath, jsonFilePath):
        """
            Description:
                function make_json converts the csv file into json file.
            Parameter:
                declaring data{} as a global variable. it will accept the json data which got converted from csv.
                csvReader to store the data which got read frrom csv file.
        """        
        try:
            data = {}
            with open(csvFilePath, encoding='utf-8') as csvf:
                csvReader = csv.DictReader(csvf)
                for rows in csvReader:
                    key = rows['StateCode']
                    data[key] = rows
            with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data, indent= 2))
        except Exception:
            print(Exception)

if __name__ == '__main__':
    # declaring an object for StateCensusData() class.
    merge_obj = StateCensusData()
    print(merge_obj.census_count())
    print(merge_obj.code_count())
    # declaring an object for Dictionary() class.
    dic_obj = Dictionary()
    dic_obj.dictionary_data()
    dic_obj.make_json(os.getenv('NEW_CODE_CENSUS_PATH'),os.getenv('JSON_PATH'))