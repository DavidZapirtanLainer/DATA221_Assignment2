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

    #Adding all tokens that are greater than 2 letters long and are composed of alphabetic characters
    if token.isalpha() and len(token) >= 0:
        list_of_tokens.append(token)

word_counts = Counter(list_of_tokens)

top_10_most_frequent_words = word_counts.most_common(10)

for word, count in top_10_most_frequent_words:
    print(f"{word} -> {count}")

sample_text_file.close()
