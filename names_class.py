class Newusers():
    def __init__(self, name):
        self.name = name

    def person_info(self):
        with open(f"{self.name.strip()}.txt", 'r') as file_to_read:
            info = file_to_read.readlines()
            print(info)

