from names_class import *

try:
    with open("names.txt", 'r') as file_to_read:
        lines = file_to_read.read().splitlines()
        for line in lines:
            user_input = input(f'information on {line} ')
            if user_input == 'exit':
                break
            else:
                line = Newusers(line)
                line.add_info(user_input)
                print(line.name)
                line.person_info()
except FileNotFoundError as error:
    print('OMG I BIFFED IT')
finally:
    print('\nThere we have our finished list')

