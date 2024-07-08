import random
import json
import time

while True:
    num = random.randint(1, 10000)  # generates random number
    with open('prng-service.txt', 'r', encoding="utf-8") as f:
        read_data = f.read()

    if read_data == 'run':
        time.sleep(3)
        with open('prng-service.txt', 'w', encoding="utf-8") as f:  # opens randomNumber.txt for writing
            f.write(json.dumps(num))  # writes the random num to the text file, as a string
