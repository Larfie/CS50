from cs50 import get_string
import re


def main():
    # Gets text input and counts letters, words and sentences
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    print(letters)
    print(words)
    print(sentences)

    # Calculates the index
    index = 0.0588 * (letters * 100 / words) - 0.296 * (sentences * 100 / words) - 15.8

    # Prints the result
    if index >= 16:
        print("Grade 16+")
    elif index <= 1:
        print("Before Grade 1")

    print("Grade {:.0f}".format(index))


# Function to count letters
def count_letters(text):
    return len(re.findall("([A-Za-z])", text))


# Function to count words
def count_words(text):
    # counts number of words in string
    length = len(text)
    nwords = 0

    #  if lenght of string is 0, there is no words
    if len == 0:
        return 0
    else:
        prevchar = text[0]

    # loops through all characters in string if encounters a space or end, and previous
    # character is not a space, counts a word
    for i in range(length):
        if (text[i] == " " or i == length - 1) and prevchar != " ":
            nwords += 1
        prevchar = text[i]
    return nwords


# Function to count sentences
def count_sentences(text):
    length = len(text)
    nsentences = 0

    # if lenght of string is 0, there is no sentences
    if len == 0:
        return 0

    # loops through all characters in string if encounters a '.', '!' or '?' counts a sentence
    # there is periods in other contexts count is going to be incorect
    for i in range(length):
        if text[i] == '.' or text[i] == '!' or text[i] == '?':
            nsentences += 1
    return nsentences


if __name__ == "__main__":
    main()
