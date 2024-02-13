# Function that reads a text file and return a count
# of the amount of unique
def count_words(path):

    # Initialize count variable to keep count of the
    # amount of unique words in a specified text file
    count = 0

    # Open file in read mode
    with open(path, "r", encoding="utf-8") as file:

        # Store all words as unique items (as lower caps) in the set(words)
        # after stripping all spaces
        words = {str(word) for word in file.read().strip().lower().split()}

        # Iterate through each unique word in the set of words
        for word in words:
            count += 1  # Increment count by 1 for each word found
        return count  # Return count of words


# Function that returns a dictionary with every word
# from a text file and the frequency of it´s occurence
def frequency_calculator(path):

    # Intialize an empty dictionary to store the words and count
    dictionary = {}

    # Open file in read mode
    with open(path, "r", encoding="utf-8") as file:

        # Read all words in the file (as lower)
        # and store them in a list (seperated)
        words = file.read().strip().lower().split()

        # Iterate through each word in the words list
        for word in words:
            # Intialize count variable to keep track of
            # the amount of characters in each word
            length = 0

            # Iterate through each character in the word
            for char in word:
                if char.isalpha():
                    length += 1
                # If there are 5 letters in the word, add word to dictionary
                # with count 1, if word is found in dictionary, increment count
                if length == 5:
                    dictionary[word] = dictionary.get(word, 0) + 1
                    break  # Break out of the inner for loop
    return dictionary


# Function to be used as the sorting key
# The 'item' argument is expected to be a tuple (key, value)
# The function returns the value (item[1]), which will be used for sorting
def sort_by_value(item):
    return item[1]


def get_top10(input_dict):
    # Sort the items in the dictionary based on their values (frequencies)
    # input_dict.items() returns a list of key-value tuples from the dictionary
    # The key function 'sort_by_value' tells Python to sort these tuples based
    # on their second element (value)
    # 'reverse=True' sorts the items in descending order so
    # that the most frequent items come first
    sorted_dict = sorted(input_dict.items(), key=sort_by_value, reverse=True)

    # Get the first 10 items from the sorted list of tuples
    # This gives us the top 10 most frequent words and their frequencies
    return sorted_dict[:10]
