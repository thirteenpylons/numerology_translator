"""
A program that will translate your name into numbers using numerology
standards.

Using the Pythagorean Method
Single digit numbers are added together individually(29:: 2+9=11)
There are three double digit numbers that do not get added(11,22,33)
These are called "Master numbers"

will need to verify each letter is alpha

Parameters:
Preconditions:

Author: Christian M. Fulton
Date: 28.April.2022
Modified: 11.May.2022

"""

##
# TODO: handle:: None value, integer value, symbol, spaces
##

def main() -> None:
    """
    Run me baby
    """
    pass


def convertString(word: str) -> str:
    """
    
    """
    converted_letters = []
    for letter in word:
        letter = convertToLower(letter)
        converted_letters.append(convertToInt(letter))
    return converted_letters


def convertToLower(letter: str) -> str:
    """
    converts the string to lower case and nothing more.
    """
    return letter.lower()


def convertToInt(letter: str) -> int:
    """
    Convert a single letter into an integer
    This must NOT manipulate the string value in any way

    Parameter letter: must be a single letter(a to z) in string format
    Preconditions: must be string value
    """
    one = ("a", "j", "s")
    two = ("b", "k", "t")
    three = ("c", "l", "u")
    four = ("d", "m", "v")
    five = ("e", "n", "w")
    six = ("f", "o", "x")
    seven = ("g", "p", "y")
    eight = ("h", "q", "z")
    nine = ("i", "r")
    if letter in one:
        return 1
    elif letter in two:
        return 2
    elif letter in three:
        return 3
    elif letter in four:
        return 4
    elif letter in five:
        return 5
    elif letter in six:
        return 6
    elif letter in seven:
        return 7
    elif letter in eight:
        return 8
    elif letter in nine:
        return 9
    else:
        return 0
