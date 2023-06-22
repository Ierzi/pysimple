
"""Gives modifications, new functions and better syntax to python. This is PySimple."""

# ------------------------------------------------------------------------------------------------
# Imports

from math import *
from random import (
    randrange, 
    choice
)
import Errors
from time import (
    sleep, 
    time
)
import typing

from typing import (
    Literal
)
import sys
import json

x = time()

# -------------------------------------------------------------------------------------------------
# Specials Variables

__version__ = "Open_B1" # B for Beta
__version_news__ = "Corrected bugs, and added the list maker"
__version_date__ = "20/06/23"
__beta_testers__ = None
__donators__ = None # Donate on my buymeacoffee.com <3

__author__ = "Ierzi"

# ------------------------------------------------------------------------------------------------
# Pi Collections

def return_pi():
    return pi

def return_simpler_pi():
    return 3.1415926535

def return_really_simple_pi():
    return 3.14159

def return_simplest_pi():
    return 3.14

def return_not_a_pi():
    return 3

# -----------------------------------------------------------------------------------------------
# Random Functions

def modify_str(word: str, *, uppercase: bool = False, lowercase: bool = False):
    """Create a copy of the modified string"""
    # I will probably make this into a class
    
    if uppercase and lowercase:
        return word
    elif uppercase:
        word = word.upper()
        return word
    elif lowercase:
        word = word.lower()
        return word
    else:
        return word
    

def isin(what: str, in_: list):
    """This is already in python, but it is a much simple syntax like that"""
    if what in in_: return True
    else: return False

def coin_flip():
    choice = randrange(0, 1)
    if choice == 0:
        return False
    elif choice == 1:
        return True
    else:
        raise Errors.ProgrammingError("Programming the module error")
        
def cf():
    choice = randrange(0, 1)
    if choice == 0:
        return False
    elif choice == 1:
        return True
    else:
        raise Errors.ProgrammingError("Programming the module error")
        
# ---------------------------------------------------------------------------------
# Binary

def binary(binary_string):
    """This is a binary translator"""
    
    text = ""
    binary_list = binary_string.split()

    for binary in binary_list:
        decimal = int(binary, 2)
        character = chr(decimal)
        text += character

    return text
        
def binary_database(index: int = None):
    
    database = ["000000011111", "1001111011", "1", "101", "10001", "1011111101", "0110111", "000001", "000111000", "111001", "0001101111",
                 "0011", "1001001", "010", "11111111111111", "11111111111101"]
    
    if index == None:
        choice_ = choice(database)
        return choice_
    else:
        
        try:
            choice_ = database.pop(index)
            return choice_
        except IndexError:
            raise Errors.Index_Out_Of_Range_Error()

# --------------------------------------------------------------------------------------------------
# Decoreators
     
def return_none(func):
    """A decorator that saves some lines by returning None at the end of a function. """
    def walrus():
        func()
        return None
    
    return walrus

def block(func):
    """A decorator that blocks the function. (Very useful)"""
    def walrus():
        return 
    
    return walrus



# ---------------------------------------------------------------------------------------------------
# Bigger Functions

def typefinder(var: any = None):
    """Find the type of the variable. BROKEN"""
    if var != None:
        try:
         var = var.upper()
         return "str"
        except AttributeError:
            if var == False or var == True:
                return "bool"
            else:
                var = str(var)
                a = var.split(".")
                if a == int(var):
                    return "int"
                else:
                    return "float"
    else:
        return "none"
    
class File_Management_Error(Exception):
    def __init__(self, message: str | None = "no description provided"):
        """Exception only used for the File Management Class in pysimple.py"""
        self.message = message

    def __str__(self) -> str:
        return f"File Management Error: {self.message}"
    

class FileManagement:
    def __init__(self):
        """It's broken."""
        self.file_name = ""

    def open_file(self, file_name: str, file_type: Literal["json", None] = None):
        try:
            if file_type == None:
                self.file = open(file_name)
            elif file_type == "json":
                pass
        except FileNotFoundError:
            raise File_Management_Error("File Not Found")
        except Exception as e:
            print(e)
            sleep(0.3)
            quit()
    
    def close_file(self):
        try:
            self.file.close()
        except FileNotFoundError:
            raise File_Management_Error("File Not Found")
        except AttributeError:
            raise File_Management_Error("Open a file before")
        except Exception as e:
            print(e)
            sleep(0.3)
            quit()

    def read_lines(self):
        pass

def time_function(func):
    """A decorator that prints the time in seconds the function needs to run."""
    def walrus():
        a = time()
        func()
        b = time() - a
        print(f"The function {func.__name__} took {b} seconds to run.")
    
    return walrus()


class Timer:
    def __init__(self):
        self.time = 0
        self.t1 = 0
        self.t2 = 0

    def start(self):
        self.t1 = time()
    
    def stop(self):
        self.t2 = time()
    
    def result(self):
        self.time = self.t2 - self.t1
        return self.time


def sort_values(*values: str | list):
    """Take an unlimited amount of string / lists values and prints a list of these strings / lists values sorted by alphabetic order"""
    _list = list(*values)
    _list.sort()
    print(_list)

def create_list(
        *values: str | list,
        sorting: bool = False,
        count_print: bool = False,
        count_var: bool = False,
        find: str | None = None

    ) -> list:
    """Take an unlimited amount of string / lists values and return a list of these strings / lists."""
    _item = 0
    _list = list(values)
    if sorting:
        _list.sort()
    if count_print:
        for item in _list:
            print(item)
    if count_var:
        for item in _list:
            _item += 1
        print(f"There is {_item} items in {_list}")
    if find != None:
        try:
            finded = _list.index(find)
            print(finded)
        except ValueError:
            print(f"{find} is not  in {_list}.")
    
    return _list

def show_platform():
    return sys.platform

def show_platform_print():
    print(sys.platform)


y = time() - x
print(y)