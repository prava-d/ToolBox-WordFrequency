""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string
from heapq import nlargest


def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """

    #strips out header comments
    f = open(file_name, 'r')
    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('POIROT EXPLAINS') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]

    #the list of all the words in the text
    word_list = []

    #strips out whitespace, punctuation, and makes lowercase
    #makes into a list of words
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation + string.whitespace)
            word = word.lower()
            word_list.append(word)

    return word_list


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequently occurring
    """
    word_counts = dict()

    for word in word_list:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1

    topn = []

    for word in nlargest(n, word_counts, key=word_counts.get):
        topn.append(word)

    return topn

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)

    #code that calls two functions
    wordlist = get_word_list('MysteriousAffair.txt')
    print(get_top_n_words(wordlist, 100))
