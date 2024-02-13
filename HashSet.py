from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        # Set the initial size to 0
        self.size = 0

        # Initialize the buckets with 8 empty lists
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash_value = 0
        for i, char in enumerate(word):
            hash_value += ord(char) * (31 ** i)
        return hash_value

    # Doubles size of bucket list
    def rehash(self):
        # Calculate the new bucket size
        new_bucket_size = len(self.buckets) * 2

        # Create new empty buckets
        new_buckets = [[] for i in range(new_bucket_size)]

        # Re-distribute words from old buckets to new buckets
        for bucket in self.buckets:
            for word in bucket:
                new_bucket_index = self.get_hash(word) % new_bucket_size
                new_buckets[new_bucket_index].append(word)

        # Assign the new buckets to the hash set
        self.buckets = new_buckets

    def secondary_hash(self, old_hash):
        return (old_hash + 1)

    def add(self, word):
        # If the set is full, rehash
        if self.size == len(self.buckets):
            self.rehash()

        # Calculate the initial bucket index for the word
        hash_value = self.get_hash(word)
        bucket_index = hash_value % len(self.buckets)

        # Check if the word already exists in the initial bucket
        if word in self.buckets[bucket_index]:
            return  # Do nothing if the word is already in the bucket

        # Linear probing for collision resolution
        probe_count = 0  # Keep track of how many times we've probed
        while len(self.buckets[bucket_index]) != 0:

            # Check if the word already exists in the new bucket
            if word in self.buckets[bucket_index]:
                return  # Do nothing if the word is already in the bucket

            # Find a new bucket index
            new_hash = self.secondary_hash(hash_value + probe_count)
            bucket_index = new_hash % len(self.buckets)
            probe_count += 1

        # If we reach here, it means we found an empty bucket or
        # a bucket where the word doesn't exist yet
        self.buckets[bucket_index].append(word)
        self.size += 1

    # Returns a string representation of the set content
    def to_string(self):
        # Intialize empty list
        words = []

        # Collect all words from all buckets
        for bucket in self.buckets:
            for word in bucket:
                words.append(word)

        # Return the words as a formatted string
        return "{ " + " ".join(words) + " }"

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        # Calculate the bucket index for the word
        hash_value = self.get_hash(word)
        bucket_index = hash_value % len(self.buckets)

        # Check if the word is in the bucket
        return word in self.buckets[bucket_index]

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        # Calculate the initial bucket index for the word
        hash_value = self.get_hash(word)
        bucket_index = hash_value % len(self.buckets)

        probe_count = 0  # Keep track of how many times we've probed

        # Linear probing for collision resolution
        while len(self.buckets[bucket_index]) != 0:
            # If word is in the bucket, remove it
            if word in self.buckets[bucket_index]:
                self.buckets[bucket_index].remove(word)
                self.size -= 1
                return

            # Find a new bucket index
            new_hash = self.secondary_hash(hash_value + probe_count)
            bucket_index = new_hash % len(self.buckets)
            probe_count += 1

    # If we reach here, it means the word was not found

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        # Intialize count variable
        size = 0

        # Iterate through all buckets to find the largest one
        for bucket in self.buckets:
            if len(bucket) > size:
                size = len(bucket)
        return size

    # Returns the ratio of buckets of length zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        # Initialize count variable
        empty_buckets = 0

        # Count the number of empty buckets
        for bucket in self.buckets:
            if len(bucket) == 0:
                empty_buckets += 1

        # Calculate the ratio of empty buckets
        return empty_buckets / len(self.buckets)

    # Returns a list with all words in the set
    def as_list(self):
        # Flatten the list of lists to get all words
        return [words for words in self.buckets]
