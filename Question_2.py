import string
from collections import Counter
#Importing string and counter in order to remove punctuation and check word frequency in list

#Opening up the file to be read then using .split() to break up each word and put it in a list
sample_text_file = open("D:/datasets/sample-file.txt", "r")
file_as_string = sample_text_file.read()
token_words = file_as_string.split()


#empty lists created to store all 'tokens' and 'bigrams' later on
list_of_tokens = []
list_of_bigrams = []

for token in token_words:
    token = token.lower() #changes tokens to lowercase

    token = token.strip(string.punctuation) # Removes punctuation from beginning and end of each token

    # adding all tokens that are greater than 2 letters long and are composed of alphabetic characters
    if token.isalpha() and len(token) >= 0:
        list_of_tokens.append(token)


#Using a for loop to go through tokens and make bigrams
for i in range(0, (len(list_of_tokens) - 2)):
    bigram = list_of_tokens[i] + " " + list_of_tokens[i+1]
    list_of_bigrams.append(bigram)

#Using the counter class to get top 10 most common bigrams
bigram_counts = Counter(list_of_bigrams)
top_10_most_frequent_bigrams = bigram_counts.most_common(10)


print("Top 10 Most Common Bigrams In 'sample-file.txt':")
for bigram, count in top_10_most_frequent_bigrams:
    print(f"{bigram} -> {count}")

sample_text_file.close()
