import getpass
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_signatures = {
        'delimiter': ['00', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'ee', 'dd', 'cc', 'bb', 'aa', '00'],
        'png': ['89', '50', '4e', '47', '0d', '0a', '1a', '0a'],
        'doc': ['d0', 'cf', '11', 'e0', 'a1', 'b1', '1a', 'e1'],
        'docx': ['50', '4b', '03', '04'],
        'docx1': ['50', '4b', '03', '04', '14', '00', '06', '00'],
        'jpg': ['ff', 'd8', 'ff', 'e0', '00', '10', '4a', '46', '49', '46', '00', '01'],
        'jpg1': ['ff', 'd8', 'ff', 'db'],
        'jpg2': ['ff', 'd8', 'ff', 'ee']
    }


def find_signatures(hex_values):
    positions = []
    for key in file_signatures:
        for i in range(len(hex_values) - len(file_signatures[key]) + 1):
            if file_signatures[key] == hex_values[i:i + len(file_signatures[key])]:
                positions.append([key, str(i)])
    return positions


def get_relevant_signatures(stego_file):
    hex_values = []
    x = stego_file
    x.strip()
    with open(x, 'rb') as f:
        z = ["{:02x}".format(c) for c in f.read()]
        for y in z:
            hex_values.append(y)
    confirmed_positions = find_signatures(hex_values)
    confirmed_positions.sort(key=lambda z: z[1])
    trackers = {}
    for x in range(len(confirmed_positions)):
        if 'delimiter' in confirmed_positions[x]:
            trackers['delimiter'] = int(confirmed_positions[x][1])
            trackers[confirmed_positions[x + 1][0]] = int(confirmed_positions[x + 1][1])
        if confirmed_positions[x][1] == '0':
            trackers[confirmed_positions[x][0]] = 0
    return trackers


def get_string_from_hex(path_to_stego):
    with open(path_to_stego, 'rb') as f:
        z = ["{:02x}".format(c) for c in f.read()]
    z_string = ''.join(z)
    return z_string


def main():
    print("Open the stego file...")
    path_to_stego = filedialog.askopenfilename()
    splits = get_relevant_signatures(path_to_stego)
    desktop = "C:/Users/{}/OneDrive/Desktop/".format(getpass.getuser())

    image_type = list(splits.keys())[0]
    file_type = list(splits.keys())[2]
    image_type_final = ''.join([i for i in image_type if not i.isdigit()])
    file_type_final = ''.join([i for i in file_type if not i.isdigit()])

    # open document with all hex values
    data = get_string_from_hex(path_to_stego)

    data_image = data[:splits['delimiter'] * 2]
    data_file = data[splits['delimiter'] * 2 + len(file_signatures['delimiter']) * 2: -1]
    image_destination = desktop + "imageportion.{}".format(image_type_final)
    file_destination = desktop + "textportion.{}".format(file_type_final)

    image_file = open(image_destination, 'wb')
    pos = 0
    while pos < len(data_image):
        num = int(data_image[pos:pos + 2], 16)
        image_file.write(num.to_bytes(1, "big"))
        pos += 2

    text_file = open(file_destination, 'wb')
    post = 0
    while post < len(data_file):
        num = int(data_file[post:post + 2], 16)
        text_file.write(num.to_bytes(1, "big"))
        post += 2


if __name__ == '__main__':
    main()
