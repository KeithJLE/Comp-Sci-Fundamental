# Lab 4
#
# Name: Keith Lee
# Instructor: Sussan Einakian
# Section: 7

import driver

def letter(row, col):
    if row == 0 or row == 8 or (3 <= row <= 5 and 3 <= col <= 6):
        return "W"
    else:
        return "S"


if __name__ == '__main__':
	driver.comparePatterns(letter)