
def get_positive_numbers():
    """
    This function reads from the user a series of numbers separated by commas and returns only the positive numbers
    the user entered.
    :return: an iterator (returned by filter) of the positive elements that the user entered.
    """
    # Converts the input string to list of ints.
    input_numbers_list = list(map(int, input("Please enter a series of numbers separated by commas: ").split(",")))
    return filter(lambda n: n > 0, input_numbers_list)


if __name__ == '__main__':
    result = get_positive_numbers()
    print(tuple(result))
