def is_even_or_odd():
    while True:
        try:
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")
            break
        except ValueError:
            print("Invalid input. Please enter an integer number.")

is_even_or_odd()