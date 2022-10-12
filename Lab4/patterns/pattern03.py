# Lab 4
#
# Name: Keith Lee
# Instructor: Sussan Einakian
# Section: 7

import driver

def letter(row, col):
    if col <= 9:
        return "D"
    else:
        return "P"

if __name__ == '__main__':
	driver.comparePatterns(letter)