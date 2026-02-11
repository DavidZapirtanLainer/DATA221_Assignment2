def find_lines_containing(filename, keyword):
    #empty list to hold lines that have keyword, the function will return this
    matches = []

    # Use lowercase for the keyword once so we don't repeat it in the loop
    search_term = keyword.lower()

#Using exception handling in case file does not exist
    try:
        with open(filename, 'r') as file:
            #Enumerate starts the count at 1
            for line_num, line_text in enumerate(file, 1):
                #Clean up the line and check for the keyword
                clean_line = line_text.strip()
                if search_term in clean_line.lower():
                    matches.append((line_num, clean_line))

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        exit() #Exits program when file error occurs

    return matches


#Example of the function

file_to_search = 'D:/datasets/sample-file.txt'
word_to_find = 'data'

lines_with_keyword = find_lines_containing(file_to_search, word_to_find)

#Print how many matching lines were found
print(f"Found {len(lines_with_keyword)} lines containing '{word_to_find}':")


#Print the first 3 matching lines (line number and text)
# We use slicing [:3] to get only the first three items

print("First 3 lines with keyword: '" + word_to_find + "'")
for line_num, text in lines_with_keyword[:3]:
    print(f"Line {line_num}: {text}")