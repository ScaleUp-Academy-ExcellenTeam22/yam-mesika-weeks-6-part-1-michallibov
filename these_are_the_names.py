
def full_names(first_names: list, last_names: list, min_length=0) -> list:
    """
    This function gets a list of names, list of last names and an optional parameter of min_length - which is
    going to be 0 by default. The function will create a list of all possible combinations of the names and the last
    names. The function will then return a list of the full names that are longer (or at the same length) than (as) the
    min_length.
    :param first_names: A list of first names that the user entered.
    :param last_names: A list of last names that the user entered.
    :param min_length: An optional parameter which is 0 by default. Only full names that are longer or equal to the
    value of this parameter will be returned in the list.
    :return: A list of full names that are longer or equals the min_length parameter.
    """
    return [first_name.title() + " " + last_name.title() for first_name in first_names for last_name in last_names
            if len(first_name + last_name) >= min_length]


if __name__ == '__main__':
    print(full_names(['avi', 'moshe', 'yaakov'], ['cohen', 'levi', 'mizrahi'], 10))
