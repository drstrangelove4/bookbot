"""
Title: boot.dev Guided Project 1
Purpose: Takes a text file in. Sums the total words and the a-z character count.
Author: drstrangelove4 & boot.dev
"""


PATH = "books/frankenstien.txt"
MODE = "r"


# ------------------------------------------------------------------------------------------------------------------------
def print_results(total_words):
    """
    A function that iterates over the dictionary values. Takes the a-z characters and prints, to the console,
    the frequency those characters appear in desending order (most frequent to least).
    """

    # create a list of dictionaries. Scrub non a-z characters from the results.
    alphabet_characters_total = []
    for entry in character_dict:
        if entry.isalpha():
            alphabet_characters_total.append(
                {"character": entry, "amount": character_dict[entry]}
            )

    # sort the dictionary - the most frequent char first.
    sorted_list = sorted(
        alphabet_characters_total, key=lambda i: i["amount"], reverse=True
    )

    # Print the results to the console.
    print(f"There are a total of {total_words} words in {PATH}.")
    for entry in sorted_list:
        print(f"The character {entry['character']} appeared {entry['amount']} times.")


# ------------------------------------------------------------------------------------------------------------------------
def count_characters(string_in):
    """
    Function takes a string as input and records the amount of times each character appears in the string via updating
    a global dictionary.
    """
    for letter in string_in:
        if letter.lower() in character_dict:
            character_dict[letter.lower()] += 1
        else:
            character_dict[letter.lower()] = 1


# ------------------------------------------------------------------------------------------------------------------------
def count_words(string_in):
    """
    Takes a string as an input. Returns an int which is the value of the number of words found in the input string.
    """
    # Split the string into individual words
    split_string = string_in.split()
    # Take the length of the string and return the value
    word_count = len(split_string)
    return word_count


# ------------------------------------------------------------------------------------------------------------------------
def main():
    """
    Prints the Frankenstien novel and its total number of words to console.
    """

    # Open the text file holding the novel data and create a list with each line as an entry.
    with open(PATH, MODE) as file:
        content = file.readlines()

    total_words = 0

    # Make the character dictionary global to remove the need to need to merge the values of 2 dictionaries
    # (the count characters function would have to return one if this was local)
    global character_dict
    character_dict = {}

    # Call functions for each line of the book.
    for line in content:
        total_words += count_words(line)
        count_characters(line)

    # Print values to console.
    print_results(total_words=total_words)


# ------------------------------------------------------------------------------------------------------------------------
main()
