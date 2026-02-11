import pandas as pd

#Taking the csv info and turning it into a data frame
student_information = pd.read_csv("D:/datasets/student.csv")

#Filtering out values from certain indices in the data frame to get desired information
#Also makes new copy
filtered_student_information = student_information[
    (student_information['studytime'] >= 3) &
    (student_information['internet'] == 1) &
    (student_information['absences'] <= 5)
].copy()

#Save the filtered data to a csv file
filtered_student_information.to_csv('high_engagement.csv', index=False)


#Print the number of students and their average grade
num_students = len(filtered_student_information)
avg_grade = (filtered_student_information['grade']).mean()

print(f"Number of students saved: {num_students}")
print(f"Average grade of filtered students: {avg_grade:.2f}")



