# CPE 101-01
# LAB 6: String Functions
# Name: Keith Lee
# Section: 7
# Date: 2/7/2022

# 1) purpose: This function takes a string as a parameter and returns a string of the vowels in the string in the order that they appear.
# signature: str -> str:
def vowel_extractor(string: str) -> str:
    new_string = ""
    for character in string:
        if ord(character) == 65 or ord(character) == 69 or ord(character) == 73 or ord(character) == 79 or ord(character) == 85 or ord(character) == 97 or ord(character) == 101 or ord(character) == 105 or ord(character) == 111 or ord(character) == 117:
            new_string = new_string + character
    return new_string


# 2) purpose: This function takes a string as a parameter and returns a new string where the first letter of each word
# in the input string starts with an uppercase letter.
# signature: str -> str:
def str_capitalize(string: str) -> str:
    new_string = ""
    idx = 0
    for character in string:
        if idx == 0 and 97 <= ord(string[idx]) <= 122:
            new_string += chr(ord(string[idx]) - 32)
        elif idx > 0 and idx != (len(string) - 1) and string[idx] == " ":
            new_string += chr(ord(string[idx]))
            if 97 <= ord(string[idx+1]) <= 122:
                new_string += chr(ord(string[idx+1]) - 32)
        elif 97 <= ord(string[idx]) <= 122 and string[idx-1] == " ":
            idx += 1
            continue
        else:
            new_string += character
        idx += 1
    return new_string


# 3) purpose: This function takes a string as a parameter and returns a new string where each letter is replaced with
# the 13th letter after it in the alphabet. The rotation is only within letters of the same case.
# signature: str -> str:
def str_rotate(string: str) -> str:
    new_string = ""
    for character in string:
        if character == " ":
            new_string = new_string + character
        elif 65 <= ord(character) <= 90 - 13:
            new_string = new_string + chr(ord(character) + 13)
        elif 90 - 13 < ord(character) <= 90:
            new_string = new_string + chr(ord(character) - 26 + 13)
        elif 97 <= ord(character) <= 122 - 13:
            new_string = new_string + chr(ord(character) + 13)
        elif 122 - 13 < ord(character) <= 122:
            new_string = new_string + chr(ord(character) - 26 + 13)
        else:
            new_string += character
    return new_string


# 4) purpose: This function takes a string and three integer numbers as input. The function returns a substring that
# begins from start index (inclusive) and ends at stop index (exclusive) and increasing step characters (positive int).
# signature: str int int int -> str:
def make_substring(s1: str, start: int, end: int, step: int) -> str:
    new_string = ""
    for i in range(start, end, step):
        new_string = new_string + s1[i]
    return new_string


# 5) purpose: This function takes a string as input and returns True if the string is a palindrome and returns False if
# it isn't.
# signature: str -> bool:
def is_palindrome(string: str) -> bool:
    for i in range(len(string)):
        if string[i] != string[-i-1]:
            return False
    return True


# 6) purpose: This function takes a string and a character as input and returns how many times the character(including
# uppercase and lowercase) was repeated in the string. If the character was not used in the string it will return -1.
# signature: str str -> int:
def count_characters(string: str, check: str) -> int:
    counter = 0
    for i in range(len(string)):
        if ord(string[i]) == ord(check):
            counter = counter + 1
    if counter == 0:
        return -1
    else:
        return counter
