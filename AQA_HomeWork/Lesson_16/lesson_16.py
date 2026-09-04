

def find_log_entries(name):
    with open("data_test/application.log", "r") as file:
        for line in file:
            if name in line:
                print(line)


find_log_entries("ERROR")
