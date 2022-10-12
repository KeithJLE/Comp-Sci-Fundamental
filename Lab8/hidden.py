# purpose: This function writes the header information into the new file.
# signature: none -> none
def write_header():
    fin = open("hidden.ppm", "r")
    fout = open("discovered.ppm", "w")
    for line in range(3):
        fout.write(fin.readline())
    fin.close()
    fout.close()


# purpose: This function writes the new pixel values into the new file.
# signature: none -> none
def add_pixel_values():
    fin = open("hidden.ppm", "r")
    for line in range(3):
        fin.readline()
    fout = open("discovered.ppm", "a")
    counter = 0
    value = None
    for pixel in fin:
        col = pixel.split()
        for idx in range(len(col)):
            if counter % 3 == 0:
                value = int(col[idx]) * 10
                if value > 255:
                    value = 255
            counter += 1
            fout.write("{}\n".format(value))
    fin.close()
    fout.close()

def main():
    write_header()
    add_pixel_values()

if __name__ == '__main__':
    main()
