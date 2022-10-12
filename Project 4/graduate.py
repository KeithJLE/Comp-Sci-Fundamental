# Project 4 – Graduate Rate (2017-2018)
# Name: Keith Lee
# Instructor: Dr. S. Einakian
# Section: 7
# main program
from graduate_funcs import *


def main():
    data = read_file("graduate_rate.csv")

    data_s = remove_extra_spaces(data)
    data_s_c = remove_extra_commas(data_s)

    graduates = create_graduate(data_s_c)
    divisions = create_division(data_s_c)

    create_files(graduates, "agriculture.csv", 2)
    create_files(graduates, "computer.csv", 4)
    create_files(graduates, "education.csv", 6)
    create_files(graduates, "engineering.csv", 8)

    total_cd = total_for_computer_division("computer.csv")
    avg_female_and_male_computer = avg_male_female_computer(graduates)
    total_all = total_for_all_majors(graduates)
    total_avg = find_total_avg(divisions, graduates)
    total_cd_by_all = total_computer_division_divided_by_total_all_majors(total_cd, total_avg)

    print_info(total_cd, avg_female_and_male_computer, total_all, total_cd_by_all)


if __name__ == "__main__":
    main()
