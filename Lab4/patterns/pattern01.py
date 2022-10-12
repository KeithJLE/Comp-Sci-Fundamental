# Lab 4
#
# Name: Keith Lee
# Instructor: Sussan Einakian
# Section: 7

import driver

def letter(row, col):
	if row % 2 == 0:
		if col <= 2:
			return "L"
		else:
			return "G"
	else:
		if 17 <= col <= 19:
			return "O"
		else:
			return "G"


if __name__ == '__main__':
	driver.comparePatterns(letter)