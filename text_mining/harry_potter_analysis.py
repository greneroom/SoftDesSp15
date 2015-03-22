__author__ = 'davidabrahams'

import file_handler #nice job importing other functions
from pattern.en import sentiment
import matplotlib.pyplot as plt
from numpy import mean


def dict_by_character(list_of_quotes):
    """
    :param list_of_quotes: a list of character, quote pairs [(char_name, quote), (char_name, quote)]
    :return: a dict that maps from char_name to a list of (line_number, quote) pairs {char_name:[(line_number, quote), (line_number, quote)]}
    """
    d = {}
    for index, (char, quote) in enumerate(list_of_quotes):
        d.setdefault(char, []).append((index, quote))
    return d


def get_character_sentiment_vs_time(character_name, dictionary):
    """
    :param character_name: the character whose sentiment we want data for
    :param dictionary: the dictionary that maps from char_name to a list of (line_number, quote) pairs
    :return: a tuple of line_numbers, sentiments. The line_numbers and sentiments lists do not contain the line_number and sentiment for quotes with sentiment = 0.0
    """
    return [x[0] for x in dictionary[character_name] if sentiment(x[1])[0] != 0.0], [sentiment(quote[1])[0] for quote in dictionary[character_name] if sentiment(quote[1])[0] != 0.0]


def convert_time_and_sentiment_to_moving_average(time_and_sentiment, window):
    """
    >>> convert_time_and_sentiment_to_moving_average(([0, 2, 4, 4, 6], [8, 8, 4, 6, 2]), 2) #Nice job with doctests
    ([1.0, 3.0, 4.0, 5.0], [8.0, 6.0, 5.0, 4.0])
    :param time_and_sentiment: a tuple of line_numbers, sentiments
    :param window: how many terms the moving average should be over
    :return: a tuple of moving_avg_line_numbs, moving_avg_sentiments, where len(moving_avg_line_numbs) and len(moving_avg_sentiments) = len(time_and_sentiment[0]) - window + 1 and len(time_and_sentiment[1] - window + 1
    """
    # unpack stuff
    time = time_and_sentiment[0]
    sent = time_and_sentiment[1]

    # create the return variables
    new_time = [None] * (len(time) - window + 1)
    new_sent = [None] * (len(time) - window + 1)

    # loop through and create the moving averages
    for i in range(len(new_time)):
        new_time[i] = mean(time[i:i+window])
        new_sent[i] = mean(sent[i:i+window])

    return new_time, new_sent

def plot_hp_trio(file_name, smoothing):
    # create the dictionary mapping from char_name to quotes
    dictionary = dict_by_character(file_handler.file_to_chars_and_quotes(file_name))

    # get the data to plot for the trio
    harry = get_character_sentiment_vs_time('HARRY', dictionary) #You could probably put all of this in a loop
    ron = get_character_sentiment_vs_time('RON', dictionary)
    hermione = get_character_sentiment_vs_time('HERMIONE', dictionary)
    malfoy = get_character_sentiment_vs_time('DRACO', dictionary)

    # take a moving average
    harry = convert_time_and_sentiment_to_moving_average(harry, smoothing) #this too, shorter code is usually better code
    ron = convert_time_and_sentiment_to_moving_average(ron, smoothing)
    hermione = convert_time_and_sentiment_to_moving_average(hermione, smoothing)
    malfoy = convert_time_and_sentiment_to_moving_average(malfoy, smoothing)

    # plot things
    plt.plot(harry[0], harry[1], label='Harry')
    plt.plot(ron[0], ron[1], label='Ron')
    plt.plot(hermione[0], hermione[1], label='Hermione')
    plt.ylabel('Sentiment level')
    plt.xlabel('Line number')
    plt.title("HP1")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    plot_hp_trio('scripts/hp1.txt', 5)
