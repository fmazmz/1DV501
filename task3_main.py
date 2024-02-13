import BstMap as bst
import HashSet as hset
import os
import time


def populate_hash_set(file_path, word_set):
    # Initialize a variable to store the zero bucket ratio
    zero = 1

    # Open file in read mode
    with open(file_path, 'r', encoding='utf-8') as file:
        print(f"Reading words from ...{os.path.basename(file_path)}")

        # Iterate through all words in the files and add them to
        # the hash set
        for word in file.read().strip().lower().split():
            word_set.add(word)

            # Return the zero bucket ratio before rehashing
            if word_set.get_size() == word_set.bucket_list_size() - 1:
                zero = word_set.zero_bucket_ratio()
    return zero


def populate_bst_map(file_path, bst_map):
    # Loop through all words in Brian file
    with open(file_path, 'r', encoding='utf-8') as file:
        for word in file.read().strip().lower().split():
            length = 0

            # Iterate through each characther
            for char in word:
                if char.isalpha():  # If char is a letter
                    length += 1  # Increment length
                if length == 5:  # If length of word is at least 5

                    value = bst_map.get(word)
                    # Check if word is already in tree
                    if bst_map.get(word):
                        bst_map.put(word,  value + 1)
                    else:
                        bst_map.put(word, 1)
                    break


def get_top_10(lst):
    """Sort and return the top 10 most used words"""
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst[:10]


def print_hash_status(file_path, hash_set):
    """Print statistics about a hash set."""
    print(f"\nHashSet Results for {file_path}:")
    print("-" * 50)
    print(f"Total unique words:\t {hash_set.get_size()}")
    print(f"Bucket List Size:\t {hash_set.bucket_list_size()}")
    print(f"Max Bucket Size:\t {hash_set.max_bucket_size()}")


def print_bst_status(file_path, bst_map):
    """Print statistics about a BST Map."""
    print(f"\nBST Results for {file_path}:")
    print("-" * 50)
    print(f"Tree Nodes:\t {len(bst_map.as_list())}")
    print(f"Max Depth:\t {bst_map.max_depth()}")
    print(f"Internal Node Count:\t {bst_map.count_internal_nodes()}")


# Program Starts

# Get Current Working Directory
cwd = os.getcwd()

# Construct the full path of the text files
path1 = os.path.join(cwd + "/data/brian_13431_words.txt")
path2 = os.path.join(cwd + "/data/news_15096801_words.txt")


# Initialize hash sets
word_set_brian = hset.HashSet()
word_set_brian.init()
word_set_swe = hset.HashSet()
word_set_swe.init()

# Initialize BST maps
bst_map_brian = bst.BstMap()
bst_map_swe = bst.BstMap()

# Start Timer
start_time = time.time()

# Populate Hash Sets
zero_bucket_ratio_brian = populate_hash_set(path1, word_set_brian)
zero_bucket_ratio_swe = populate_hash_set(path2, word_set_swe)

# Populate BST's
populate_bst_map(path1, bst_map_brian)
populate_bst_map(path2, bst_map_swe)

# Print Hash Statistics
print_hash_status(os.path.basename(path1), word_set_brian)
print(f"Zero Bucket Ratio:\t {round(zero_bucket_ratio_brian, 3)}")
print_hash_status(os.path.basename(path2), word_set_swe)
print(f"Zero Bucket Ratio:\t {round(zero_bucket_ratio_swe, 3)}")
print_bst_status(os.path.basename(path1), bst_map_brian)
print_bst_status(os.path.basename(path2), bst_map_swe)

# Retrieve the top ten words from the BST map
top_ten_words_brian = get_top_10(bst_map_brian.as_list())
top_ten_swe = get_top_10(bst_map_swe.as_list())

# Print the top ten words
print("\nTop 10 Words from Brian's BST:")
print("-" * 50)
for word, frequency in top_ten_words_brian:
    print(f"Word: '{word}', Frequency: {frequency}")

print("\nTop 10 Words from Swedish News BST:")
print("-" * 50)
for word, frequency in top_ten_swe:
    print(f"Word: '{word}', Frequency: {frequency}")

# End Timer
end_time = time.time()
# Calculate elapsed time
elapsed_time = end_time - start_time
# Print elapsed time
print(f"\nRuntime: {round(elapsed_time, 2)} seconds to run.\n")
