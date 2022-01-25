#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 24, 2022
# This program is a basic calculator that
# asks for the operator and two numbers


def calculate(sign, first_number, second_number):
    # This function calculates the operation between both chosen numbers

    if sign == "+":
        total = (first_number + second_number)
    elif sign == "-":
        total = (first_number - second_number)
    elif sign == "/":
        total = (first_number / second_number)
    elif sign == "*":
        total = (first_number * second_number)
    else:
        total = (first_number % second_number)
    return(total)


def main():
    # this gets the user input and then calls the function

    print("This program is a basic calculator. It can add, subtract, " +
          "multiply, divide, and find the remainder of division.")
    print(" ")
    print(" ")

    while True:
        # Get user input for the first number
        first_number_from_user = input("Enter your first number: ")
        # Make sure that the input is a number
        try:

            first_number_from_user_float = float(first_number_from_user)

            # Get user input for the second number
            second_number_from_user = input("Enter your second number: ")
            print(" ")
            # Make sure that the input is a number
            try:
                # Get user input for base
                second_number_from_user_float = float(second_number_from_user)

                # Get user input for the operator
                sign_from_user = input("Enter the operator that " +
                                       "you'd like to use (+, -, /, *, %): ")
                print("")

                if sign_from_user == "+" or sign_from_user == \
                    "-" or sign_from_user == "/" or sign_from_user \
                        == "*" or sign_from_user == "%":
                    # Call the function
                    final_answer = calculate(sign_from_user,
                                             first_number_from_user_float,
                                             second_number_from_user_float)

                    print("{} {} {} = {}".format(first_number_from_user,
                                                 sign_from_user,
                                                 second_number_from_user,
                                                 final_answer))
                    break
                else:
                    print("Operator must be either +, -, /, * or %")

            # Print error message if input is invalid
            except Exception:
                print("Input must be a number")
        # Print error message if input is invalid
        except Exception:
            print("Input must be a number")

        print("")


if __name__ == "__main__":
    main()
