""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string
import re
from collections import Counter


def split_line_into_lowercase_list(s):
    """ Returns the a list of strings, where each string is a word from the list.
    Words are defined by any sequence of alpha characters or apostraphes

    >>> split_line_into_lowercase_list("This is a sentence.")
    ['this', 'is', 'a', 'sentence']
    >>> split_line_into_lowercase_list("This can't be split.")
    ['this', "can't", 'be', 'split']
    >>> split_line_into_lowercase_list("These.words-should_be;seperated.")
    ['these', 'words', 'should', 'be', 'seperated']
    >>> split_line_into_lowercase_list("Don't include 1 2 3 4 5 6 7 8 9")
    ["don't", 'include']
    """

    # Use a regular expression, searching for all reptitions of a-z characters or 's
    return re.findall(r"[a-zA-Z']+", s.lower())


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
        punctuation, and whitespace are stripped away.  The function
        returns a list of the words used in the book as a list.
        All words are converted to lower case.
    """
    # open the file object
    file_obj = open(file_name, 'r')
    # read it into a list of strings
    lines = file_obj.readlines()
    # find the index of the line right after the line containing 'START OF THIS PROJECT GUTENBERG EBOOK'
    start_line = next(i for i, s in enumerate(lines) if 'START OF THIS PROJECT GUTENBERG EBOOK' in s) + 1
    #we only care about the book itself
    lines = lines[start_line + 1:]

    words = []
    for line in lines:
        word_list = split_line_into_lowercase_list(line)
        words.extend(word_list)

    return words


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words (assumed to all be in lower case with no
                    punctuation
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequentlyoccurring
    """
    counter = Counter(word_list)
    most_common_words = [c[0] for c in counter.most_common(n)]
    return most_common_words


def main():
    print get_top_n_words(get_word_list('pg32325.txt'), 100)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()