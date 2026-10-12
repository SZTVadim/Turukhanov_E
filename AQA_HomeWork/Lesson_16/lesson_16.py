def find_log_entries(name):
    with open("/Users/edoo1995/Desktop/AQA Python/Turukhanov_E/data_test/application.log", "r") as file:
        for line in file:
            if name in line:
                print(line)


find_log_entries("ERROR")
