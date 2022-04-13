import time


def timer(f, *iterables):
    """
    This function counts down the amount of time it took to finish the run of function f.
    :param f: The function that we want to run and count down how much time did it take it to finish it's run.
    :param iterables: A list of arguments that we want to pass to the function f
    :return: The amount of time it took to function f to finish it's run.
    """
    time_function_started_running = time.time()
    # Run the function f on each element in the iterables
    map(f, iterables)
    time_function_finished_running = time.time()
    return time_function_finished_running - time_function_started_running


if __name__ == '__main__':
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
