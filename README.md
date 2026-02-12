# DATA221_Assignment2
This repository contains the python files for each of the questions in Assignment 2 for DATA221, this file will contain a summary 
of each question in the assignment.

Question 1: 
After importing the string and counter class, this code opens up the sample.txt file then collects each word in the file as a list. 
An instance of counter is used in order to find the top 10 most frequent words or "tokens" within the text file.

Question 2:
Similar to the first question, the string and counter class are imported. The code in question two also reads the sample.txt file
and saves each word as an element of a list, however instead of finding the most common "token"s for loop logic is used to find 
the 5 most common "bigrams" which are collections of 2 words rather than one. 

Question 3: 
After importing the string and collections modules, this code opens a text file and reads it line by line. Each line is normalized
by removing punctuation, whitespace, and uppercase letters so similar lines can be compared. A defaultdict is then used to group 
lines with the same normalized form and identify sets of near-duplicate lines in the file.

Question 4:
After importing the pandas library, this code reads student data from a CSV file into a DataFrame. The data is then filtered to
include only students with high study time, internet access, and low absences. The filtered results are saved to a new CSV file,
and the number of selected students along with their average grade is printed.

Question 5: 
After importing pandas, this code reads student data from a CSV file into a data frame. The grade column is divided into Low,
Medium, and High bands using pd.cut. The data is then grouped by grade band to calculate the number of students, average
absences, and percentage with internet access, and the summary table is saved to a new CSV file.

Question 6: 
After importing pandas, this code reads crime data from a CSV file into a DataFrame. The violent crime rate is divided into 
LowCrime and HighCrime categories using pd.cut. The data is then grouped by crime level to calculate the average unemployment 
rate for each category, and the results are converted to percentages and displayed.

Question 7: 
After importing requests and BeautifulSoup, this code sends a request to the Wikipedia Data Science page and parses the HTML 
content. It extracts and prints the page title, then searches the main content section for the first paragraph with at least 50
characters and displays it.

Question 8: 
After importing requests and BeautifulSoup, this code retrieves the Wikipedia Data Science page and parses its HTML content. It
extracts all main section headings, excludes sections like References and External links, and saves the remaining headings to a 
text file.

Question 9: 
After importing requests, BeautifulSoup, and csv, this code retrieves the Machine Learning Wikipedia page and parses its HTML
content. It extracts the first table with at least three rows, formats the data with appropriate headers, and saves the 
structured results to a CSV file.

Question 10:
This code defines a function that searches a text file for lines containing a given keyword. It returns the matching line 
numbers and text, handles file errors using exception handling, and prints the total matches along with the first three results.




