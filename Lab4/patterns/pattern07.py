# Lab 4
#
# Name: Keith Lee
# Instructor: Sussan Einakian
# Section: 7

import driver

def letter(row, col):
    if row == 10:
        return "B"
    elif 2 <= row <= 5 and 4 <= col <= 9:
        if 4 <= row <= 5 and 7 <= col <= 9:
            return "X"
        else:
            return "Y"
    elif 4 <= row <= 6 and 7 <= col <= 12:
        return "B"
    else:
        return "K"


if __name__ == '__main__':
	driver.comparePatterns(letter)