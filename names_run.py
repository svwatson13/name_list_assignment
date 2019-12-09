from names_class import *

try:
    with open("names.txt", 'r') as file_to_read:
        lines = file_to_read.read().splitlines()
        for line in lines:
            line = Newusers(line)
            print(line.name)
            line.person_info()
except FileNotFoundError as error:
    print('OMG I BIFFED IT')
finally:
    print('\nThere we have our finished list')

