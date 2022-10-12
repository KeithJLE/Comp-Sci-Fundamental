# signature: none -> list
# purpose: This function opens the file, removes the \n, and adds each line in a file to a list. The function returns this new list.
def convert_to_list(file_name) -> list[str]:
    try:
        fin = open("{}".format(file_name), "r")
    except Exception:
        print("Unable to open {}".format(file_name))
        exit()
    L1 = []
    for line in fin:
        info = ""
        info += line
        L1.append(info.replace("\n", ""))
    return L1


# signature: list -> list
# purpose: This function takes a list of strings and separates them based on spaces. The function returns this new list.
def separate_spaces(L: list[str]) -> list[str]:
    newL = []
    for line in L:
        sublist = line.split()
        newL += sublist
    return newL


# signature: list -> int int int
# purpose: This function checks whether a string in a list represents an int or float and adds one to its corresponding counter.
# If it is neither of those, the "other" counter will increase by one. The function returns a tuple of those three counters.
def check_value(L: list[str]) -> tuple[int, int, int]:
    ints = 0
    floats = 0
    other = 0
    for idx in range(len(L)):
        if L[idx].isdigit():
            ints += 1
        else:
            try:
                L[idx] = float(L[idx])
                floats += 1
            except ValueError:
                other += 1
    return ints, floats, other


# signature: int int int -> none
# purpose: This function prints the amount of integers, floats, and other from the file read in the beginning.
def print_info(ints: int, floats: int, other: int) -> None:
    print("Ints: {} \nFloats: {} \nOther: {}".format(ints, floats, other))


if __name__ == '__main__':
    L1 = convert_to_list("infile")
    L2 = separate_spaces(L1)
    ints, floats, other = check_value(L2)
    print_info(ints, floats, other)