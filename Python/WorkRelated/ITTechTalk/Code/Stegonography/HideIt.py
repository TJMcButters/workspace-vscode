import tkinter as tk
from tkinter import filedialog
from os.path import join
import os
import getpass

root = tk.Tk()
root.withdraw()
image_size = 0
file_size = 0
combined_size = 0


def main():
    image_ext = ''
    path_to_desktop = os.path.join("C:/Users/{}/OneDrive/Desktop/").format(getpass.getuser())

    print("Open your image file... ")
    path_to_image = filedialog.askopenfilename()
    if path_to_image == '':
        print("You didn't select an image, exiting...")
        exit()
    else:
        image_size = os.path.getsize(path_to_image)
    for let in range(len(path_to_image)):
        if '.' == path_to_image[let]:
            image_ext = path_to_image[let + 1:]

    print("Open the file you would like to hide... ")
    path_to_file = filedialog.askopenfilename()
    if path_to_file == '':
        print("You didn't select a file, exiting...")
        exit()
    else:
        file_size = os.path.getsize(path_to_file)

    new_name = input("What would you like to call the new document: ") + '.' + image_ext

    out = open(join(path_to_desktop, new_name), "wb")
    out.write(open(path_to_image, "rb").read())

    hex_as_bytes = b"\x00\xaa\xbb\xcc\xdd\xee\xff\xee\xdd\xcc\xbb\xaa\x00"
    out.write(hex_as_bytes)

    out.write(open(path_to_file, "rb").read())
    out.close()

    new_file = path_to_desktop + new_name
    hex_list = []
    """
    with open(new_file, 'rb') as f:
        hex_list = ["{:02x}".format(c) for c in f.read()]
    print(hex_list[:10])
    """
    values = open(join(path_to_desktop, "hexvalues.txt"), 'w')
    values.write(str(hex_list).replace('\'', '').replace('[', '').replace(']', '').replace(',', '').replace(' ', ''))
    values.close()

    combined_size = os.path.getsize(new_file)
    print("The original image size is: {} Bytes\nThe original file size is: {} Bytes\nAnd the new combined size is: {} Bytes".format(image_size, file_size, combined_size)) 


if __name__ == '__main__':
    main()
