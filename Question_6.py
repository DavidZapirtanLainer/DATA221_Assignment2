import pandas as pd

crime_dataset = pd.read_csv("D:/datasets/crime.csv")

#Making bin limits and labels to help create table for later on
risk = ["LowCrime", "HighCrime"]
bins_for_risk = [-1, 0.5, 1]

#Using pd.cut to break up the grade column into the new bins we just created
#Right = False parameter used to make sure 0.5 is collected in the high crime bin
crime_dataset['risk_band'] = pd.cut(crime_dataset['ViolentCrimesPerPop'], bins=bins_for_risk, labels=risk, right=False)


unemployment_per_risk_group = crime_dataset.groupby('risk_band').agg({
    'PctUnemployed': 'mean',
}).reset_index() #Make sure LowCrime and High Crime are in a column and not the index

#Taking proportion of unemployed and turning it into percent by multiplying by 100,
#ALso rounded to 2 decimal places as a stylistic decision
unemployment_per_risk_group['PctUnemployed'] = round(unemployment_per_risk_group["PctUnemployed"] * 100, 2)


#Renaming Columns
unemployment_per_risk_group.columns = ["Crime Level", "% Unemployed"]


print("AVERAGE UNEMPLOYMENT LEVELS FOR COMMUNITIES WITH DIFFERENT LEVELS OF CRIME")
print(unemployment_per_risk_group)
