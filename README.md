# The Robert Burns Kata

## Introduction

Robert Burns was a Scottish poet and lyricist, widely regarded as the national poet of Scotland. His poetry celebrated the common people, country life, and the customs and traditions of Scotland. Burns Night, which is celebrated on January 25th, is a celebration of his life and work.

# Task

You are given a directory of text files containing poetry written by Robert Burns. Your task is to write a script that takes in the filepaths of the Burns poems as input and calculate the type-token ratio (TTR) for each poem. TTR is a measure of lexical diversity or lexical richness (for more context see https://en.wikipedia.org/wiki/Lexical_density), it's calculated by dividing the number of unique words in a text by the total number of words in the text.

For example, if a text contains 100 words and has 40 unique words, the TTR would be 0.4. The TTR can provide insight into how varied the vocabulary of a text is, with a higher TTR indicating a more varied vocabulary.

A starter example with an `argparse` and `main` construct to receive the filepath argument, open the file and print a result is provided.

### Input

A file path to the poem text file.

### Output

A float value representing the TTR of the poem.

## Hints

- To tokenize the text of each poem, you can use Python's built-in string methods such as `split()` and `replace()`, or the `re` library.
- Tokenization should be case-insensitive and handle punctuation correctly (e.g. "The" and "the," should be treated as the same word)
- To calculate the TTR of a poem, you will first need to tokenize the text of the poem and then calculate the number of unique words and the total number of words in the poem.
- The argparse library has been used to open the file of the poem passed as a command-line argument.

## Bonuses

Implement a simple [stemmer](https://en.wikipedia.org/wiki/Stemming) to preprocess the text before calculating the TTR. A stemmer is a tool that removes the suffixes from words. For example, "running" and "runner" will be stemmed to "run".

Another preprocessing step that can be included is removing stopwords, which are common words that do not contain much meaning (e.g. "the", "and", "is"). Removing stopwords can help to focus on the more meaningful words in the text.

The filenames are not the poem titles, just a sanitized version of the first line, once you have a tokenized and stemmed words with no stopwords, could you devise better filenames?

## Even More Ideas

Building a word frequency distribution: Once the text has been tokenized, you can build a word frequency distribution, which is a list of the words in the text along with the number of times each word appears. This can give a sense of the most common words used in the poem.

Part of Speech Tagging: Part-of-speech tagging, also known as grammatical tagging or word-category disambiguation, is the process of marking up a word in a text as corresponding to a particular part of speech, based on both its definition and its context. This can give a sense of the grammatical structure of the text.

Named Entity Recognition: Named-entity recognition (NER) is the process of identifying named entities in text and classifying them into predefined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.
