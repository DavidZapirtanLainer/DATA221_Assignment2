import pandas as pd

#Reading csv and turning it to dataframe
student_information = pd.read_csv("D:/datasets/student.csv")

#New Lists that will later be bins in the data frame
new_labels_for_grades = ["Low", "Medium", "High"]
new_grades_bins = [-1, 9, 14, 20]

#Using pd.cut to break up the grade column into the new bins we just created
student_information['grade_band'] = pd.cut(student_information['grade'], bins=new_grades_bins, labels=new_labels_for_grades)

#Aggregating number of students for each bin, the average absences for each student based on grade band
#As well as the proportion of students that have access to internet in each grade band
summary = student_information.groupby('grade_band').agg({
    'grade': 'count',
    'absences': 'mean',
    'internet': 'mean'
}).reset_index()

#Turn the decimal into a percentage by multiplying by 100
summary['internet'] = summary['internet'] * 100

#Renaming the columns
summary.columns = ['grade_band', 'number_of_students', 'average_absences', 'percentage_with_internet']

#Saving the table to a csv file
summary.to_csv('student_bands.csv', index=False)

print(summary)

