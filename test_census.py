import pytest
from State_analyser import StateCensusAnalyser, CSVStates
import os
from dotenv import load_dotenv
load_dotenv()

def test_census_count():
    """
        Description:
            function test_census_count test the count of row in a csv file data
        Parameter:
            define count_census variable which accept the argument of path and operation to perform
        assert:
            testing the count of row that matches with given count 29
    """    
    count_census = StateCensusAnalyser()
    assert count_census.census_count() == 29

def test_code_count():
    """
        Description:
            function test_code_count test the count of row in a csv file data
        Parameter:
            define count_code variable which accept the argument of path and operation to perform
        assert:
            testing the count of row that matches with given count 37
    """        
    count_code = CSVStates()
    assert count_code.code_count() == 37

def test_census_path():
    """
        Description:
            function test_census_path test the path of a file that is to be called 
        Parameter:
            define path_check variable which accept the path which is provide to read the csv file
        assert:
            testing the given file path with actually path location
    """    
    path_check = os.getenv("CENSUS_PATH")
    assert path_check == 'E:\CFA\python\Indian_Census\StateCensusData.csv'

def test_code_path():
    """
        Description:
            function test_code_path test the path of a file that is to be called 
        Parameter:
            define path_check variable which accept the path which is provide to read the csv file
        assert:
            testing the given file path with actually path location
    """    
    path_check = os.getenv("CODE_PATH")
    assert path_check == 'E:\CFA\python\Indian_Census\StateCode.csv'

def test_census_file_type():
    """
        Description:
            function test_census_file_type test the path of a file that is to be called 
        Parameter:
            define given_file variable which accept the path which is provide the file extension 
        assert:
            testing the given file extention with actually 'csv' extention
    """
    given_file = os.getenv("CENSUS_PATH")
    assert 'csv' in given_file

def test_code_file_type():
    """
        Description:
            function test_code_file_type test the path of a file that is to be called 
        Parameter:
            define given_file variable which accept the path which is provide the file extension 
        assert:
            testing the given file extention with actually 'csv' extention
    """    
    given_file = os.getenv("CODE_PATH")
    assert 'csv' in given_file