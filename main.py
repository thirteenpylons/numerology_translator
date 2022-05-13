"""
A program that will translate your name into numbers using numerology
standards.

Using the Pythagorean Method
Single digit numbers are added together individually(29:: 2+9=11)
There are three double digit numbers that do not get added(11,22,33)
These are called "Master numbers"

This takes the entire string and strips spaces and computes as one.
#! Will be interesting to have capability to compute multiple names
    and return list of integers from all names

#! TODO compute birthdates(include number computations)

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
    usr_in = input("Enter the word(s) to convert: ")
    if cleanString(usr_in).isalpha(): # remove whitespace from string verify alpha
        converted_string = convertString(usr_in)
        converted_sum = sum(converted_string)
        print(pyMethod(converted_sum))
        return pyMethod(converted_sum)
    else:
        return "Invalid input."


def cleanString(string:str) -> str:
    """
    clean whitespace out of the string.
    """
    return string.replace(" ", "")


def convertString(word: str) -> list:
    """
    Take a string and convert each letter in string to integer
    and return list of integer values.

    Parameter word:
    Preconditions:
    """
    converted_letters = []
    for letter in word:
        letter = convertToLower(letter)
        converted_letters.append(convertToInt(letter))
    return converted_letters


def convertToLower(letter: str) -> str:
    """
    converts the string to lower case and nothing more.
    
    This is used in the convertString() func
    """
    return letter.lower()


def convertToInt(letter: str) -> int:
    """
    Convert a single letter into an integer
    This must NOT manipulate the string value in any way

    This is used in convertString() func

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


# something different?
def newConvertToInt(this_letter: str) -> int:
    """
    Convert a single letter into an integer
    This must NOT manipulate the string value in any way

    This is used in convertString() func

    Parameter letter: must be a single letter(a to z) in string format
    Preconditions: must be string value
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    count = 1
    for letter in letters:
        if count > 9:
            count = 1
        if letter == this_letter:
            return count
        count += 1




def pyMethod(number: int) -> int:
    """
    Add together until get to single digit or(11,22,33)
    """
    while number > 9:
        if number == 33:
            return 33
        elif number == 22:
            return 22
        elif number == 11:
            return 11
        number = sum(int(i) for i in str(number))
    return number
        

if __name__ == "__main__":
    main()
