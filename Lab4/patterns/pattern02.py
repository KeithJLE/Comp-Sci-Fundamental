# Lab 4
#
# Name: Keith Lee
# Instructor: Sussan Einakian
# Section: 7

import driver

def letter(row, col):
	if 0 <= row <= 4 or 8 <= row <= 9:
		return "N"
	elif 5 <= row <= 7:
		if 5 <= col <= 10:
			return "M"
		else:
			return "N"
	elif 13 <= row <= 15:
		if 5 <= col <= 10:
			return "M"
		else:
			return "Z"
	else:
		return "Z"


if __name__ == '__main__':
	driver.comparePatterns(letter)