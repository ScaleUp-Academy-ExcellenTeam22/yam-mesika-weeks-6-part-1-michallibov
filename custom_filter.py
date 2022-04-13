
def my_filter(function, iterable) -> list:
    """
    This function is an override to the known function 'filter'. It gets a function we
    want to run on each element, and an iterable object that we will run the function on.
    :param function: A function we want to run on an iterable object we received
    :param iterable: An iterable object that we want to run a function on each element in it
    :return: returns A list comprehension of all the elements in the iterable object that if
    we run on them the function we received we will get 'True'.
    """
    if function is None:
        result = [iterator for iterator in iterable if iterator]
    else:
        result = [iterator for iterator in iterable if function(iterator)]
    return result


if __name__ == '__main__':
    to_sum = [0, "", None, 0.0, True, False, "Hello"]
    equivalent_to_true = my_filter(None, [1, -2, 0])
    print(tuple(equivalent_to_true))
