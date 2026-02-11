import string
from collections import Counter
#Importing string and counter in order to remove punctuation and check word frequency in list

#Opening up the file to be read then using .split() to break up each word and put it in a list
sample_text_file = open("D:/datasets/sample-file.txt", "r")
file_as_string = sample_text_file.read()
token_words = file_as_string.split()

list_of_tokens = [] #Empty file created to store all 'tokens' later on

for token in token_words:
    token = token.lower() #Changes tokens to lowercase

    token = token.strip(string.punctuation) #Removes punctuation from beginning and end of each token

    # Checking that each token has at least 2 alphabetic characters
    alphabetic_characters = [char for char in token if char.isalpha()]
    if len(alphabetic_characters) >= 2:
        list_of_tokens.append(token)

word_counts = Counter(list_of_tokens)

top_10_most_frequent_words = word_counts.most_common(10)

for word, count in top_10_most_frequent_words:
    print(f"{word} -> {count}")

sample_text_file.close()
for word, count in top_10_most_frequent_words:
    print(f"{word} -> {count}")

sample_text_file.close()

