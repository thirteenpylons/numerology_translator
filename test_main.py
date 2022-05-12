"""
Tests for main
"""
from main import *

##
# test cases:: None value, symbol, spaces, integer value
##
FIRST_NAME = "Christian"
MIDDLE_NAME = "Michael"
LAST_NAME = "FULTON"
WHOLE_NAME = "Christian Michael Fulton"

EXPECT_CLEAN_WHOLE_NAME = "ChristianMichaelFulton"

EXPECT_FIRST_NAME_LOWER = "christian"

EXPECT_FIRST_NAME_LIST = [3, 8, 9, 9, 1, 2, 9, 1, 5]
EXPECT_MIDDLE_NAME_LIST = [4, 9, 3, 8, 1, 5, 3]
EXPECT_LAST_NAME_LIST = [6, 3, 3, 2, 6, 5]
EXPECT_WHOLE_NAME_LIST = []

EXPECT_FIRST_NAME_ADDED = 11
EXPECT_MIDDLE_NAME_ADDED = 33
EXPECT_LAST_NAME_ADDED = 7
EXPECT_WHOLE_NAME_ADDED = 6

FAILING_STRINGS = ["& #@%TGD DF FE#Rfd"]
# test the main function
def test_main():
    pass


def test_cleanString():
    """
    Expected to remove space from string.
    """
    print("Testing cleanString()...")
    assert cleanString(WHOLE_NAME) == EXPECT_CLEAN_WHOLE_NAME
    print("cleanString() Passed.")


def test_convertString():
    """
    Expected to return a list of integers
    """
    print("Testing convertString()...")
    assert convertString(FIRST_NAME) == EXPECT_FIRST_NAME_LIST
    print("convertString Passed.")


def test_convertToLower():
    """
    Expected to convert to lowercase
    """
    print("Testing convertToLower()...")
    assert convertToLower(FIRST_NAME) == EXPECT_FIRST_NAME_LOWER
    print("convertToLower() Passed.")


def test_convertToInt():
    """
    Expected to convert single letter to integer
    """
    print("TestingconvertToInt()...")
    letters = "abcdefghijklmnopqrstuvwxyz"
    count = 1
    for letter in letters:
        if count > 9:
            count = 1
        assert count == convertToInt(letter)
        count += 1
    print("convertToInt passed.")