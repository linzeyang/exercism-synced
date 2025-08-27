def is_armstrong_number(number):
    number_string = str(number)
    num_of_digits = len(number_string)
    return sum(int(char) ** num_of_digits for char in number_string) == number
