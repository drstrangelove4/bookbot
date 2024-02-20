from pprint import pprint

PATH = "books/frankenstien.txt"
MODE = 'r'


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

    # Print out the content of each entry in the content list.
    for line in content:
        # print(line)
        total_words += count_words(line)
        count_characters(line)

    # Print values to console.
    print(f"Word count: {total_words}")
    pprint(character_dict)


# ------------------------------------------------------------------------------------------------------------------------
main()
