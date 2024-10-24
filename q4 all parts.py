# Problem-4: Magical Collection of Characters
magical_collection = ('F', 'l', 'a', 'b', 'b', 'e', 'r', 'g', 'a', 's', 't', 'e', 'd')

# a) Add an exclamation point at the end
magical_collection += ('!',)

# b) Extract ('b', 'b') from the tuple
extracted = magical_collection[3:5]

# c) Transform the collection into a single string
magical_string = ''.join(magical_collection)

# d) Count occurrences of 'e'
count_e = magical_collection.count('e')

# e) Check if 'r' exists
has_r = 'r' in magical_collection

# f) Transform the collection into a list
magical_list = list(magical_collection)

# g) Remove 'b', 'e', and 'r'
for char in ['b', 'e', 'r']:
    magical_list = [x for x in magical_list if x != char]

print(magical_list)
