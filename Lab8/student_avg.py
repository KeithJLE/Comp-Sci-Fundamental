# purpose: This function creates a list from the file information we are looking at.
# signature: none -> list
def create_list():
    fin = open("std_info.txt", "r")
    info_list = []
    for line in fin:
        info_list += line.split()
    fin.close()
    return info_list


# purpose: This function takes the major and list of the file info as parameters to find the average score of each major.
# signature: list str -> float
def find_avg_major(info_list, major):
    sum = 0
    counter = 0
    for idx in range(len(info_list)):
        if info_list[idx] == major:
            sum += float(info_list[idx+1])
            counter += 1
        idx += 1
    return sum/counter


# purpose: This function takes the list of the file info to find the average score of all majors.
# signature: list -> float
def find_avg_total(info_list):
    sum = 0
    counter = 0
    for idx in range(len(info_list)):
        if (idx-3) % 4 == 0:
            sum += float(info_list[idx])
            counter += 1
    return sum/counter


# purpose: This function creates a new file with the information from the old student information file.
# signature: none -> none
def write_file():
    fin = open("std_info.txt", "r")
    fout = open("student_avg.txt", "w")
    for line in fin:
        fout.write(line)
    fout.close()
    fin.close()


# purpose: This function takes the EE avg, CPE avg, and the total avg and appends the information to the new file created in the write_file function.
# signature: float float float -> none
def write_averages(EE_avg, CPE_avg, total_avg):
    fout = open("student_avg.txt", "a")
    fout.write("EE average = {:0.2f}\nCPE average = {:0.2f}\nTotal average = {:0.2f}".format(EE_avg, CPE_avg, total_avg))
    fout.close()


def main():
    info_list = create_list()
    EE_avg = find_avg_major(info_list, "EE")
    CPE_avg = find_avg_major(info_list, "CPE")
    total_avg = find_avg_total(info_list)
    write_file()
    write_averages(EE_avg, CPE_avg, total_avg)


if __name__ == '__main__':
    main()
