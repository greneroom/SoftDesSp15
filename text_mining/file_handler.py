import re

__author__ = 'davidabrahams'


def get_string_from_file(file_name):
    """
    :param file_name: a string of the file name to read
    :return:= a string of the text within than file
    """
    return open(file_name).read()


def is_word_before_all_caps(string, index_of_colon):
    """
    >>> is_word_before_all_caps('HARRY: I love magic', 5)
    True
    >>> is_word_before_all_caps("Flamel: I'm immortal", 6)
    False
    >>> is_word_before_all_caps('Now space : I love magic', 10)
    False

    :param string: the string to check
    :param index_of_colon: the index of the colon to look before
    :return: if the word directly before the colon is in all caps
    """
    index = index_of_colon
    while index >= 0 and not string[index].isspace():
        index -= 1
    return string[index+1:index_of_colon].isupper()


def char_name(string, index_of_colon):
    """
    The name of the character starts right after the first '\n' before the ':' that follows his name

    :param string: the string to look through
    :param index_of_colon: the index of the colon to look before
    :return: the name of the character preceding the ':"

    >>> char_name("he said.\\nDUMBLEDORE: Stuff", 19)
    'DUMBLEDORE'
    >>> char_name("end quote. \\nProf Mc: Stuff", 19)
    'Prof Mc'
    """

    # Look backward for the first whitespace occurrence to determine the character's name
    first_whitespace = index_of_colon
    while first_whitespace >= 0 and not string[first_whitespace] == '\n':
        first_whitespace -= 1
    return string[first_whitespace + 1:index_of_colon]


def find_quote(string, index_of_colon):
    """
    >>> find_quote("HARRY: Good job!\\nDUMBLEDORE: Second, to Mr. Ronald ", 5)
    'Good job!'
    >>> find_quote("LEE JORDAN: We won!\\n---------\\nScene", 10)
    'We won!'
    >>> find_quote("HARRY: I'm not going home. Not really.\\n----------\\nScene 35: End Credits.\\n\\n                                   -The End-\\n\\n", 5)
    "I'm not going home. Not really."


    :param string: the string to look through
    :param index_of_colon: the index of the colon that indicates the start of a quote
    :return: a string of the quote the character said
    """

    # look for the next speaking character and section break
    next_colon = string.find(': ', index_of_colon + 2)
    while next_colon != -1 and not char_name(string, next_colon).isupper():
        next_colon = string.find(': ', next_colon + 2)
    next_break = string.find('---------', index_of_colon + 2)

    # if there is no next speaking character or section break, assume the quote spans the rest of the file
    if next_break == -1 and next_colon == -1:
        end_of_quote = len(string)
    else:
        # if we didn't find either a colon or a break, the quote ends at the one we found
        if next_colon == -1:
            end_of_quote = next_break
        elif next_break == -1:
            end_of_quote = next_colon
        # if we found both, the quote ends at the first one
        else:
            end_of_quote = min(next_colon, next_break)

        # end the character's quote at the next new line
        while end_of_quote >= 0 and string[end_of_quote] != '\n':
            end_of_quote -= 1

    # extract the quote and strip leading and trailing whitespace
    quote = string[index_of_colon + 2:end_of_quote].strip()
    # replace characters like \n, \t, with spaces
    quote = re.sub("[\s]+", " ", quote)
    # return it!
    return quote


def file_to_chars_and_quotes(file_name):
    """
    :param file_name: the name of the file to get quotes from
    :return: a list of tuples [(char_name, quote), (char_name, quote)]
    """

    # get the text from the file
    string = get_string_from_file(file_name)
    # initialize the return variable and where we will be searching
    char_quote_pairs = []
    start_looking_at = 0

    # search until we cannot find another ': '
    while string.find(': ', start_looking_at) != -1:

        colon_loc = string.find(': ', start_looking_at)

        # The name of the character starts right after the first whitespace before the ':' that follows his name
        char = char_name(string, colon_loc)

        # It's only a character name if it only contains capital letters
        if char.isupper():
            # find the quote
            quote = find_quote(string, colon_loc)

            # append the character name and quote to the return variable
            char_quote_pairs.append((char, quote))

            # increment the loop control
            start_looking_at = colon_loc + len(quote)
        else:
            # if this ': ' does not indicate a character, quote pair, keep looking
            start_looking_at = colon_loc + 2

    return char_quote_pairs

if __name__ == '__main__':
    import doctest
    doctest.testmod()