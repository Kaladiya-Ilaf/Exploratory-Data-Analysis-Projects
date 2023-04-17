import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline - used in notebooks (google colab / jupyter) only.

import mysql.connector
from decouple import config


from preprocessing import retrun_statistics, seperate_columns_numerical_categorical

data = pd.read_csv("/home/ilaf/Desktop/EDA_Projects/HRAnalytics/dataSource/HR-Employee-Attrition.csv", encoding_errors = "ignore")
print(retrun_statistics(data))

categoical_cols, numerical_cols = seperate_columns_numerical_categorical(data)
print("\nCategorical columns : ", categoical_cols)
print("\nNumerical columns : " , numerical_cols)

mydb = mysql.connector.connect(
				host = config("host"),
				port = config("port"),
				user = config("user"),
				password = config("password"),
				database = config("database")
			       )

print("Connection Successful !!!")
print("Instance : ", mydb)

mycursor = mydb.cursor()
for Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager in  zip(data['Age'],data['Attrition'],data['BusinessTravel'],data['DailyRate'],data['Department'],data['DistanceFromHome'],data['Education'],data['EducationField'],data['EmployeeCount'],data['EmployeeNumber'],data['EnvironmentSatisfaction'],data['Gender'],data['HourlyRate'],data['JobInvolvement'],data['JobLevel'],data['JobRole'],data['JobSatisfaction'],data['MaritalStatus'],data['MonthlyIncome'],data['MonthlyRate'],data['NumCompaniesWorked'],data['Over18'],data['OverTime'],data['PercentSalaryHike'],data['PerformanceRating'],data['RelationshipSatisfaction'],data['StandardHours'],data['StockOptionLevel'],data['TotalWorkingYears'],data['TrainingTimesLastYear'],data['WorkLifeBalance'],data['YearsAtCompany'],data['YearsInCurrentRole'],data['YearsSinceLastPromotion'],data['YearsWithCurrManager']):
	sql = "INSERT INTO HRData(Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager)
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")












