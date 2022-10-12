# purpose: This function prints the information from the file we are looking at.
# signature: none -> none
def print_info():
    fin = open('in.txt', 'r')
    line_number = 0
    for line in fin:
        line_number += 1
        characters = len(line) - 1
        print('Line {} ({} chars): {}'.format(line_number, characters, line), end='')
    fin.close()


if __name__ == '__main__':
    print_info()
