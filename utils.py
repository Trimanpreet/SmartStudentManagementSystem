def get_integer(message):

    while True:

        try:
            value = int(input(message))
            return value

        except ValueError:
            print("Please enter a valid number.")


def get_float(message):

    while True:

        try:
            value = float(input(message))
            return value

        except ValueError:
            print("Please enter a valid number.")
