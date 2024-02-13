import HashSet as hset

# Program starts

# Initialize word set
words = hset.HashSet()   # Create new empty HashSet
words.init()             # Initialize with eight empty buckets

# Add names to word set. Notice: a) contains duplicate names,
# b) more than eight names ==> will trigger rehash
names = ["Ahmad", "Daniel", "Sebastian", "Bjorn", "Hedda", "Ahmad", "Gyaawa", "Gyaawa", "Rodions", "Jonas", "Ola", "Karen", "Tobias", "Tobias", "Hedda", "Samuel", "Seif", "Marek", "Emma"]
print("\nAdded names:", len(names))
for name in names:
    words.add(name)

print("\nto_string():", words.to_string())  # { Ahmad Seif Marek Bjorn Samuel Sebastian Hedda Tobias Rodions Daniel Jonas Gyaawa Ola Emma Karen }
print("get_size():", words.get_size())             # 15
print("contains(Hedda):", words.contains("Hedda"))   # True
print("contains(Hobbe):", words.contains("Hobbe"))     # False

# Hash specific data
mx = words.max_bucket_size()
print("\nmax bucket:", mx)                # 3
buckets = words.bucket_list_size()
print("bucket list size:", buckets)     # 16
zero_buckets_ratio = words.zero_bucket_ratio()
print("zero bucket ratio:", round(zero_buckets_ratio, 2))  # 0.5

# Remove elements
delete = ["Bjorn", "Ola", "Tobias", "Jonas", "Ola"]
for s in delete:
    words.remove(s)
print("\nget_size:", words.get_size())   # 11
print("as_list():", words.as_list())   # ['Ahmad', 'Seif', 'Marek', 'Samuel', 'Sebastian', 'Hedda', 'Rodions', 'Daniel', 'Gyaawa', 'Emma', 'Karen']
