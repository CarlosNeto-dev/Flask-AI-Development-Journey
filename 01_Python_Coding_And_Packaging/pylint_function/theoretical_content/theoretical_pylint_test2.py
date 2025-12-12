# Cria um arquivo ".py" e permite o usar a funcionalidade "pylint".
"""This archive talks about the principal logical of program!"""

def sum_of_numbers(num1, num2):
    """
    :param num1: The first number of the sum.
    :param num2: The second number of the sum.
    :return: Return the sum num1 + num2
    """
    return num1 + num2


def main():
    """
    The main function of the program.
    """
    number1 = float(input("Type the first number: ").strip())
    number2 = float(input("Type the second number: ").strip())
    print(f"The sum is: {sum_of_numbers(number1, number2)}! ")


if __name__ == "__main__":
    main()
