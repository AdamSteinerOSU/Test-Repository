import time
import os

while True:
    user_input = input('Enter 1 to generate a new image, Enter 2 to Exit: ')  # get user input

    if user_input == '1':
        with open('prng-service.txt', 'w', encoding="utf-8") as f:  #
            f.write("run")

        time.sleep(5)

        with open('prng-service.txt', 'r', encoding="utf-8") as f:
            read_data = f.read()

        time.sleep(5)

        with open('image-service.txt', 'w', encoding="utf-8") as f:
            f.write(read_data)

        time.sleep(5)

        with open('image-service.txt', 'r', encoding="utf-8") as f:
            image_data = f.read()

        time.sleep(3)

        os.startfile(image_data)
    elif user_input == '2':
        break
