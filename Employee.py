def create_employee_file():
    file_name = "employee.txt"
    try:
        with open(file_name, "w") as file:
            print("Employee File Created: ", file_name)
    except IOError:
        print("Error: Unable to create file.")

def add_employee():
    file_name = "employee.txt"
    try:
        with open(file_name, "a") as file:
            employee_name = input("Enter employee name: ")
            employee_address = input("Enter employee address: ")
            file.write(f"Name: {employee_name}, Address: {employee_address}\n")
            print("Employee details added successfully!")
    except IOError:
        print("Error: Unable to write to file.")

def main():
    create_employee_file()
    add_employee()

if __name__ == "__main__":
    main()bhaurao