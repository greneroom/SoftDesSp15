__author__ = 'davidabrahams'

import file_handler
from pattern.en import sentiment
import matplotlib.pyplot as plt
from numpy import mean


def dict_by_character(list_of_quotes):
    d = {}
    for index, (char, quote) in enumerate(list_of_quotes):
        d.setdefault(char, []).append((index, quote))
    return d

def get_character_sentiment_vs_time(character_name, dict):
    return [x[0] for x in dict[character_name] if sentiment(x[1])[0] != 0.0], [sentiment(quote[1])[0] for quote in dict[character_name] if sentiment(quote[1])[0] != 0.0]


def convert_time_and_sentiment_to_moving_average(time_and_sentiment, window):
    """
    >>> convert_time_and_sentiment_to_moving_average(([0, 2, 4, 4, 6], [8, 8, 4, 6, 2]), 2)
    ([1.0, 3.0, 4.0, 5.0], [8.0, 6.0, 5.0, 4.0])
    :param time_and_sentiment:
    :param window:
    :return:
    """
    time = time_and_sentiment[0]
    sent = time_and_sentiment[1]
    new_time = [None] * (len(time) - window + 1)
    new_sent = [None] * (len(time) - window + 1)
    for i in range(len(new_time)):
        new_time[i] = mean(time[i:i+window])
        new_sent[i] = mean(sent[i:i+window])
    return new_time, new_sent

def plot_hp_trio(file_name, smoothing):
    dict = dict_by_character(file_handler.file_to_chars_and_quotes(file_name))
    harry = get_character_sentiment_vs_time('HARRY', dict)
    ron = get_character_sentiment_vs_time('RON', dict)
    hermione = get_character_sentiment_vs_time('HERMIONE', dict)
    harry = convert_time_and_sentiment_to_moving_average(harry, smoothing)
    ron = convert_time_and_sentiment_to_moving_average(ron, smoothing)
    hermione = convert_time_and_sentiment_to_moving_average(hermione, smoothing)

    plt.plot(harry[0], harry[1], label='Harry')
    plt.plot(ron[0], ron[1], label='Ron')
    plt.plot(hermione[0], hermione[1], label='Hermione')
    plt.ylabel('Sentiment level')
    plt.xlabel('Line number')
    plt.title("Sorcerer's Stone")
    plt.legend()
    plt.show()



if __name__ == '__main__':
    plot_hp_trio('scripts/hp1.txt', 10)