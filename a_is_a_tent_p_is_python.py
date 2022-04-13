
def get_letters() -> list:
    """
    This function returns a list of all the abc letters from 'a' to 'z' and then 'A' to 'Z'.
    :return: A list of all the letters in the abc. First the lowercase letters and then the uppercase.
    """
    answer = [chr(letter) for letter in range(ord('a'), ord('z') + 1)] + \
             [chr(letter) for letter in range(ord('A'), ord('Z') + 1)]
    return answer


if __name__ == '__main__':
    print(get_letters())
