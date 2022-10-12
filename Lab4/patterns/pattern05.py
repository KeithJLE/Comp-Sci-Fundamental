# Lab 4
#
# Name: Keith Lee
# Instructor: Sussan Einakian
# Section: 7

import driver

def letter(row, col):
    if 0 <= row <= 8:
        if col < row:
            return "B"
        else:
            return "U"
    elif 9 <= row <= 11:
        if 0 <= col <= 10:
            return "B"
        else:
            return "U"
    else:
        if col < row:
            return "B"
        else:
            return "U"


if __name__ == '__main__':
    driver.comparePatterns(letter)