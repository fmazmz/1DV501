import task1
import os


# Main program

# Get Current Working Directory
cwd = os.getcwd()


# Define the path of the text files
txt_file = "/data/brian_13431_words.txt"
txt_file2 = "/data/news_15096801_words.txt"

# Construct the full path of the text file
path = os.path.join(cwd + txt_file)
path2 = os.path.join(cwd + txt_file2)


# *************************Run program for file 1*************************

# Call the function count_words to return
# the amount of unique words found in the text file
print(f"\nTotal amount of words in {path}: ", end="")
print(task1.count_words(path))
print()  # New line


# Call the function frequency_calculator to return a dictionary
# with all the words that contain 4+ letters
word_dict = task1.frequency_calculator(path)

# Call the function get_top10 with a dictionary
# to return a list of the top 10 most used words
print("Top 10 most frequent words used:")
print("-----------------------------")
sorted_dict = task1.get_top10(word_dict)

# Loop through the top 10 items and print them
for word, frequency in sorted_dict:
    print(f"{word}: {frequency}")


# *************************Run program for file 2*************************

# Call the function count_words to return
# the amount of unique words found in the text file
print(f"\nTotal amount of words in {path2}: ", end="")
print(task1.count_words(path2))
print()  # New line

# Call the function frequency_calculator to return a dictionary
# with all the words that contain 4+ letters
word_dict2 = task1.frequency_calculator(path2)

# Call the function get_top10 with a dictionary
# to return a list of the top 10 most used words
print("Top 10 most frequent words used:")
print("-----------------------------")
sorted_dict2 = task1.get_top10(word_dict2)

# Loop through the top 10 items and print them
for word, frequency in sorted_dict2:
    print(f"{word}: {frequency}")
