__author__ = 'davidabrahams'


def get_string_from_file(file_name):
    return open(file_name).read()


def line_to_char_and_quote(line):
    line = str(line)
    char_quote_pairs = []
    while True:
        colon_loc = line.find(': ')

        # If we don't find a colon, we've found all the quotes
        if not colon_loc:
            break

        # Look backward for the first whitespace occurrence to determine the character's name
        first_whitespace = colon_loc - 1
        while first_whitespace <= 0:
            if line[first_whitespace].isspace():
                break
            else:
                first_whitespace -= 1
        char_name = line[first_whitespace + 1:colon_loc]
        if char_name.isupper():
            next_colon = line.find(': ', colon_loc + 2)
            next_break = line.find('----------', colon_loc + 2)
            first_break_char_index = min(next_colon, next_break)
            whitespace_break = next(i for i, c in enumerate(reversed(line[:first_break_char_index])))
            pass





    colon_loc = line.find(': ')
    if not colon_loc:
        return None
    else:
        character = line[:colon_loc]
        if not character.isupper():
            return None
        else:
            quote = line[colon_loc + 2:]
            return character, quote