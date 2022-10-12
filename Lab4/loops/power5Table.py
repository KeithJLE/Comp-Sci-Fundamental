# CPE 101 Lab 4
# Name: Keith Lee
# Section: 7

def main():
    table_size = get_table_size()
    while table_size != 0:
        first = get_first()
        increment = get_increment()
        show_table(table_size, first, increment)
        table_size = get_table_size()


# Obtain a valid table size from the user
# signature: none -> int
def get_table_size():
    size = int(input("Enter number of rows in table (0 to end): "))

    while (size) < 0:
        print("Size must be non-negative.")
        size = int(input("Enter number of rows in table (0 to end): "))

    return size;


# Obtain the first table entry from the user
# signature: none -> int
def get_first():
    first = int(input("Enter the value of the first number in the table: "))
    while first < 0:
        print("First number must be non-negative.")
        first = int(input("Enter the value of the first number in the table: "))
    return first;


# Display the table of power5
# signature: int int int -> none
def show_table(size, first, increment):
    print("A power5 table of size %d will appear here starting with %d." % (size, first))
    print("\033[4mNumber\033[0m  \033[4mPower5\033[0m")
    sum_of_power5 = 0
    for row in range(0, size):
        power5 = ((first + (increment * row)) ** 5)
        print("{0:^6d}{1:>6d}".format(first + (increment * row), power5))
        sum_of_power5 += power5
    print("The sum of power5 is: %d" % sum_of_power5)


# purpose statement: This function gets the value of the increment for the power5 table from the user and returns it.
# signature: none -> int
def get_increment():
    increment = int(input("Enter the increment between rows: "))
    while increment < 0:
        print("Input must be non-negative.")
        increment = int(input("Enter the increment between rows: "))
    return increment


if __name__ == "__main__":
    main()
