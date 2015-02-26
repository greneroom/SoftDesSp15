import re

__author__ = 'davidabrahams'


def get_string_from_file(file_name):
    return open(file_name).read()


def is_word_before_all_caps(string, index_of_colon):
    """
    >>> is_word_before_all_caps('HARRY: I love magic', 5)
    True
    >>> is_word_before_all_caps("Flamel: I'm immortal", 6)
    False
    >>> is_word_before_all_caps('Now space : I love magic', 10)
    False

    :param string:
    :param index_of_colon:
    :return:
    """
    index = index_of_colon
    while index >= 0 and not string[index].isspace():
        index -= 1
    return string[index+1:index_of_colon].isupper()


def char_name(string, index_of_colon):
    """
    The name of the character starts right after the first '\n' before the ':' that follows his name

    :param string:
    :param index_of_colon:
    :return:

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


    :param string:
    :param index_of_colon:
    :return:
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
        if next_colon == -1:
            end_of_quote = next_break
        elif next_break == -1:
            end_of_quote = next_colon
        else:
            end_of_quote = min(next_colon, next_break)

        # end the character's quote at the next new line
        while end_of_quote >= 0 and string[end_of_quote] != '\n':
            end_of_quote -= 1
    quote = string[index_of_colon + 2:end_of_quote].strip()
    quote = re.sub("[\s]+", " ", quote)
    return quote


def file_to_chars_and_quotes(file_name):
    string = get_string_from_file(file_name)
    char_quote_pairs = []
    start_looking_at = 0
    length = len(string)
    print string[6380:6450]
    while string.find(': ', start_looking_at):
        colon_loc = string.find(': ', start_looking_at)

        # If we don't find a colon, we've found all the quotes
        if colon_loc == -1:
            break

        # The name of the character starts right after the first whitespace before the ':' that follows his name
        char = char_name(string, colon_loc)

        # It's only a character name if it only contains capital letters
        if char.isupper():

            quote = find_quote(string, colon_loc)
            char_quote_pairs.append((char, quote))
            start_looking_at = colon_loc + len(quote)
        else:
            start_looking_at = colon_loc + 2
    return char_quote_pairs

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    for t in file_to_chars_and_quotes('scripts/hp2.txt'):
        print t