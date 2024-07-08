import os
import time

list_images = os.listdir(path='images')  # get a directory of the image folder

length = len(list_images)  # get length of the image folder

while True:
    with open('image-service.txt', encoding="utf-8") as f:
        read_data = f.read()  # read the random number from the text file, and save it as read_data
    if read_data.isnumeric():
        time.sleep(3)
        image_selected = int(read_data)  # convert the random number into an int
        image_selected = image_selected % length  # if i >= to number of images, modulo i by the size of the image set

        image = list_images[image_selected]  # get the selected image

        with open('image-service.txt', 'w', encoding="utf-8") as f:
            f.write('C:/CS361/images/' + image)  # write the selected image to text file