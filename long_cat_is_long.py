import re


def count_words(text: str) -> dict:
    """
    This function gets a text and returns a dictionary in which every word in the text appears only once as a key,
    and the value of each key is the length of the word. (the length of the key)
    :param text: A string which we will build a dictionary out of.
    :return: The dictionary of the string which contains all the words from the text and their length. Each word
    appears only once.
    """
    return {word: len(word) for word in re.sub(r'[^\w\s]', '', text).lower().split(" ") if word.isalpha()}


if __name__ == '__main__':
    print(count_words("You see, wire telegraph is a kind of a very, very long cat. You pull his tail in New York and "
                      "his head is meowing in Los Angeles. Do you understand this? And radio operates exactly the same "
                      "way: you send signals here, they receive them there. The only difference is that there is no "
                      "cat."))
