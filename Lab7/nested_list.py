# CPE 101-01
# LAB 7: Nested Lists
# Name: Keith Lee
# Instructor: S. Einakian
# Section: 7
# Date: 2/22/2022


# purpose: This function groups the values of the input list into groups of three. If there aren't enough values
# for the last group then it will have less than three values.
# signature: list -> list
def groups_of_3(old_list: list) -> list:
    new_list = []
    if len(old_list) % 3 == 0:
        for i in range(len(old_list)//3):
            new_list.append([old_list[3*i], old_list[3*i + 1], old_list[3*i + 2]])
    elif len(old_list) % 3 == 2:
        for i in range((len(old_list)//3)):
            new_list.append([old_list[3*i], old_list[3*i + 1], old_list[3*i + 2]])
        new_list.append([old_list[len(old_list)-2], old_list[len(old_list)-1]])
    else:
        for i in range(len(old_list)//3):
            new_list.append([old_list[3*i], old_list[3*i + 1], old_list[3*i + 2]])
        new_list.append([old_list[len(old_list)-1]])
    return new_list


# purpose: This function returns a list with only the final value of each inner list from the input list. If an inner
# list is empty, it will have no corresponding integer in the output list.
# signature: list -> list
def final_value(old_list: list) -> list:
    new_list = []
    for i in range(len(old_list)):
        for j in range(len(old_list[i])):
            if j == len(old_list[i]) - 1:  #if empty at location, len - 1 = -1, so nothing appended since j != -1
                new_list.append(old_list[i][j])
    return new_list


# purpose: This function returns a 2D list of integers where each inner list repeats its corresponding integer in the input
# list that number of times. Assume no negative numbers.
# signature: list -> list
def repeat_value(old_list: list) -> list:
    new_list = []
    for i in range(len(old_list)):
        new_list.append([old_list[i]] * old_list[i])
    return new_list
