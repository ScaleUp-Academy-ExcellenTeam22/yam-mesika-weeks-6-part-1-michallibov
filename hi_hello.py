
def words_length(sentence: str) -> list:
    """
    This function gets a sentence and returns a list of the length of each word in the given sentence.
    :param sentence: A sentence that the function will split and create a list of each word's length in it.
    :return: A list of the lengths of each word. The first word's length in the sentence will be in the first cell of
    the list, the second word's length in the sentence in the second cell, etc.
    """
    words_len = [len(word) for word in sentence.split(" ")]
    return words_len


if __name__ == '__main__':
    print(words_length("Toto, I've a feeling we're not in Kansas anymore"))
