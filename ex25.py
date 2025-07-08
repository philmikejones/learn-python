def break_words(stuff):
    """
    This function will break up words for us

    :return: The individual words in an iterable
    :rtype: list
    """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """
    Sorts the words into ascending alphabetical order
    
    :return: A sorted list of words
    :rtype: list
    """
    return sorted(words)

def print_first_word(words):
    """
    Returns the first word in the given list

    :return: A word
    :rtype: str
    """
    first_word = words.pop(0)
    return first_word

def print_last_word(words):
    """
    Returns the last word in the list

    :return: A word
    :rtype: str
    """
    last_word = words.pop(-1)
    return last_word

def sort_sentence(sentence) -> str:
    """
    Takes in a full sentence and returns the sorted words as a string (rather than a list)

    :return: The sorted sentence
    :rtype: str
    """
    sentence = break_words(sentence)
    sentence = sort_words(sentence)
    # https://stackoverflow.com/a/12453584
    sentence = ' '.join(sentence)
    return sentence

def print_first_and_last(sentence) -> str:
    """
    Prints the first and last word of the given sentence

    :return: The first and last word of the sentence
    :rtype: tuple
    """
    sentence = break_words(sentence)
    words = print_first_word(sentence), print_last_word(sentence)
    return words

def print_first_and_last_sorted(sentence) -> str:
    """
    Sorts the given sentence alphabetically then returns the first and last word
    
    :return: First and last word from the given sentence, after sorting
    :rtype: list
    """
    sentence = break_words(sentence)
    sentence = sorted(sentence)
    words = print_first_word(sentence), print_last_word(sentence)
    return words
