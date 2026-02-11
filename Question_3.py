import string
import collections

#Make a normalize function to use on lines later that puts all lines in the same format,
#Meaning no punctuation, spaces, or uppercase letters
def normalize(text):
    #Convert to lowercase
    text = text.lower()
    #Remove whitespace and punctuation
    chars_to_remove = string.whitespace + string.punctuation
    table = str.maketrans('', '', chars_to_remove)
    return text.translate(table)

#Dictionary makes empty list as item for every key created
potential_duplicate_groups = collections.defaultdict(list)

with open('D:/datasets/sample-file.txt', 'r') as f:
    for i, line in enumerate(f, 1):
        clean_line = normalize(line)
        # We only care about non-empty lines
        if clean_line:
            potential_duplicate_groups[clean_line].append((i, line.strip()))

#Filter only the sets that actually have duplicates
duplicate_sets = [lines for lines in potential_duplicate_groups.values() if len(lines) > 1]

#Print all the results
print(f"Number of near-duplicate sets: {len(duplicate_sets)}")


#Use enumerate to make first index and go through duplicate sets with for loop
for i, s in enumerate(duplicate_sets[0:2], 1):
    print(f"Set {i}:")
    for line_num, original_text in s:
        print(f"  Line {line_num}: {original_text}")