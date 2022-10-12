# Project 4 – Graduate Rate (2017-2018)
# Name: Keith Lee
# Instructor: Dr. S. Einakian
# Section: 7

from typing import Tuple, List


# purpose: This class represents a division with ID and division name from the graduate rates csv file.
class Division:
    def __init__(self, id: int, division_name: str):
        self.id = id
        self.division_name = division_name

    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Division and self.id == other.id and self.division_name == other.division_name

    def __repr__(self) -> str:
        return "ID: " + str(self.id) + ", Division Name: " + str(self.division_name)


# purpose: This class represents a graduate with ID, major, and amount of graduates for bachelor, master, and doctor from the graduate rates csv file.
class Graduate:
    def __init__(self, id: int, major: str, bachelor: tuple, master: tuple, doctor: tuple):
        self.id = id
        self.major = major
        self.bachelor = bachelor
        self.master = master
        self.doctor = doctor

    def __eq__(self, other) -> bool:
        return type(self) == type(other) == Graduate and self.bachelor == other.bachelor and self.master == other.master and self.doctor == other.doctor

    def __repr__(self):
        return "ID: " + str(self.id) + ", Major: " + str(self.major) + ", Bachelor: " + str(self.bachelor) + ", Master: " + str(self.master) + ", Doctor: " + str(self.doctor)


# purpose: This function takes a file name as input, opens the file for reading, and returns a tuple of two lists, one with the header information and one with the rest of the information from the file.
# signature: file -> tuple
def read_file(file_name) -> list:
    try:
        fin = open("{}".format(file_name), "r")
    except FileNotFoundError:
        exit("Sorry, Wrong file name!")
    data1 = []
    data2 = []
    data3 = []
    header = []
    for line in fin:
        data1.append(line)
    for string in data1:
        data2.append(string.replace("\n", ""))

    for idx in range(3):
        header.append(data2[idx])
    for idx in range(3, len(data2)):
        data3.append(" ".join(data2[idx].split()))
    fin.close()
    return data3


# purpose: This function takes a list of strings as input and returns a new list of strings with the extra spaces removed.
# signature: list -> list
def remove_extra_spaces(data: list) -> list:
    new_data = []
    for string in data:
        string_new = " ".join(string.split())
        string2 = ""
        for idx in range(len(string_new) - 1):
            if string_new[idx] == " " and string_new[idx - 1] == ":" and string_new[idx + 1].isdigit():
                string2 += string_new[idx]
            letter_is_next = (65 <= ord(string_new[idx + 1]) <= 90 or 97 <= ord(string_new[idx + 1]) <= 122)
            letter_is_before = (65 <= ord(string_new[idx - 1]) <= 90 or 97 <= ord(string_new[idx - 1]) <= 122)
            if string_new[idx] == " " and not (letter_is_next and letter_is_before):
                pass
            else:
                string2 += string_new[idx]
            if string_new[idx] == "." and string_new[idx + 1] != "/":
                string2 += " "
        if string_new[len(string_new) - 1] == " ":
            pass
        else:
            string2 += string_new[len(string_new) - 1]
        new_data.append(string2)
    return new_data


# purpose: This function takes a list of strings as input and returns a new list of strings with the extra commas removed after the extra spaces have already been removed.
# signature: list -> list
def remove_extra_commas(data: list) -> list:
    new_data = []
    for string in data:
        string2 = ""
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        for idx in range(len(string) - 1):
            letter_is_next = (65 <= ord(string[idx + 1]) <= 90 or 97 <= ord(string[idx + 1]) <= 122)
            number_is_next = string[idx + 1] in nums
            if string[idx] == "," and not (letter_is_next or number_is_next):
                pass
            else:
                string2 += string[idx]
        if string[len(string) - 1] == ",":
            pass
        else:
            string2 += string[len(string) - 1]
        new_data.append(string2)
    return new_data


# purpose: This function creates a list of Division objects from an input list of strings.
# signature: list -> list
def create_division(data: list) -> list:
    newL = []
    divisions = []
    for string in data:
        newL.append(string.split(","))
    for idx in range(len(newL)):
        if len(newL[idx]) == 2 and int(newL[idx][0]) % 100 == 0:
            divisions.append(Division(int(newL[idx][0]), newL[idx][1]))
    return divisions


# purpose: This function creates a list of Graduate objects from an input list of strings.
# signature: list -> list
def create_graduate(data: list) -> list:
    newL = []
    graduates = []
    for string in data:
        newL.append(string.split(","))
    for idx in range(len(newL)):
        if len(newL[idx]) != 2:
            graduates.append(Graduate(int(newL[idx][0]), newL[idx][1], (int(newL[idx][2]), int(newL[idx][3])),
                                      (int(newL[idx][4]), int(newL[idx][5])), (int(newL[idx][6]), int(newL[idx][7]))))
    return graduates


# purpose: This function creates a file of graduate information using the specified file name and division ID.
# signature: list str int -> none
def create_files(graduates: list, file_name: str, ID_2: int) -> None:
    try:
        name = open("{}".format(file_name), "w")
    except FileNotFoundError:
        exit("Sorry, Wrong file name!")
    name.write("This table shows Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, of student and discipline division: 2017-18" + "\n" + "ID,Major,Bachelor,Master,Doctor\n")
    for value in graduates:
        if str(value.id)[0] == "3" and str(value.id)[1] == "{}".format(ID_2) and value.id % 100 != 0:
            name.write(str(value.id) + "," + str(value.major) + "," + str(value.bachelor[0] + value.bachelor[1]) + "," +
                       str(value.master[0] + value.master[1]) + "," + str(value.doctor[0] + value.doctor[1]) + "\n")
    name.close()


# purpose: This function takes an input list of Division and Graduate objects and returns a list of tuples with the total and average graduate rate for the division.
# signature: list list -> list
def find_total_avg(divisions: list, graduates: list) -> list:
    computed_data = []
    for division in divisions:
        counter = 0
        total = 0
        for graduate in graduates:
            if str(division.id)[1] == str(graduate.id)[1]:
                counter += 1
                total += graduate.bachelor[0] + graduate.bachelor[1] + graduate.master[0] + graduate.master[1] + graduate.doctor[0] + graduate.doctor[1]
        avg = total / counter
        computed_data.append((total, float("{:.2f}".format(avg))))
    return computed_data


# purpose: This function takes as input a Graduate object with a given major and returns the male and female graduate rate.
# signature: Graduate -> str
def find_graduate_rate(graduate: Graduate) -> tuple:
    males = graduate.bachelor[0] + graduate.master[0] + graduate.doctor[0]
    females = graduate.bachelor[1] + graduate.master[1] + graduate.doctor[1]
    return males, females


# purpose: This function takes as input the file name to read the information from and returns the integer value of the total graduates under Computer and information sciences and support.
# signature: str -> int
def total_for_computer_division(file_name: str) -> int:
    sum = 0
    try:
        fout = open("{}".format(file_name), "r")
    except FileNotFoundError:
        exit("Sorry, Wrong file name!")
    fout.readline()
    fout.readline()
    for line in fout:
        newL = ""
        newL += (line.replace("\n", ""))
        newL = newL.split(",")
        sum += int(newL[2]) + int(newL[3]) + int(newL[4])
    fout.close()
    return sum


# purpose: This function takes as input a list of Graduate objects and returns a tuple of two float values for the average of male and the average of female graduates in Computer and information sciences and support.
# signature: list -> tuple
def avg_male_female_computer(graduates: list) -> tuple:
    male_sum = 0
    female_sum = 0
    counter = 0
    for graduate in graduates:
        if str(graduate.id)[1] == "4":
            counter += 1
            male_sum += graduate.bachelor[0] + graduate.master[0] + graduate.doctor[0]
            female_sum += graduate.bachelor[1] + graduate.master[1] + graduate.doctor[1]
    return male_sum / counter, female_sum / counter


# purpose: This function takes as input a list of Graduate objects and returns the total number of graduates in all the majors.
# signature: list -> int
def total_for_all_majors(graduates: list) -> int:
    sum = 0
    for graduate in graduates:
        sum += graduate.bachelor[0] + graduate.bachelor[1] + graduate.master[0] + graduate.master[1] + graduate.doctor[0] + graduate.doctor[1]
    return sum


# purpose: This function takes as input the total number of graduates in the computer division and the total number of graduates in all majors and compares them.
# The function returns a float value representing the ratio between those numbers.
# signature: int list -> float
def total_computer_division_divided_by_total_all_majors(total_computer_division: int, total_avg: list) -> float:
    total = 0
    for set in total_avg:
        total += set[0]
    return total_computer_division / total


# purpose: This function prints the information for the total graduates in the computer division, the average number of male/female
# graduates in the computer division, the total number of graduates for all majors, and the comparison between the total number of graduates for
# the computer division vs the total number of graduates for all majors. The function uses those values as inputs.
# signature: int tuple int float -> None
def print_info(total_computer_division: int, avg_female_and_male_computer_division: tuple, total_female_and_male_all_majors: int, total_computer_division_divided_by_total_all_majors: float) -> None:
    print("Total OF Processed Graduate in Computer and information sciences and support: {}".format(total_computer_division))
    print("Average of Processed Female and Male in computer and information sciences and support: Males - {:.2f}, Females - {:.2f}".format(avg_female_and_male_computer_division[0], avg_female_and_male_computer_division[1]))
    print("Total of all Females and Males Graduate in all Majors: {}".format(total_female_and_male_all_majors))
    print("Compare total graduate rate of Computer and information sciences and support to all other Majors: Ratio - {:.2f}".format(total_computer_division_divided_by_total_all_majors))