# Lab 4
#
# Name: Keith Lee
# Instructor: Sussan Einakian
# Section: 7

import driver

def letter(row, col):
    if row == 0 or row == 8 or col == 0 or col == 8:
        return "C"
    elif col == row or col == 8 - row:
        return "E"
    else:
        return "O"


if __name__ == '__main__':
	driver.comparePatterns(letter)