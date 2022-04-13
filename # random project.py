import string
import random

def chrachtr(count):

    all_chars = string.ascii_letters + string.digits

    chars_count = len(all_chars)

    serial_list =[]

    while count > 0:

        random_number = random.randint(0,chars_count-1 )

        random_chracter = all_chars[random_number]

        serial_list.append(random_chracter)

        count -=1

    print("".join(serial_list))


chrachtr(30)