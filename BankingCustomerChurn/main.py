import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline - used in notebooks (google colab / jupyter) only.

import mysql.connector
from decouple import config

from preprocessing import retrun_statistics, seperate_columns_numerical_categorical

data = pd.read_csv("/home/ilaf/Desktop/EDA_Projects/BankingCustomerChurn/data_source/Bank Customer Churn Prediction.csv", encoding_errors = "ignore")

print(retrun_statistics(data))

categoical_cols, numerical_cols = seperate_columns_numerical_categorical(data)
print("Categorical columns : ", categoical_cols)
print("Numerical columns : " , numerical_cols)

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
for customer_id , credit_score , country , gender , age , tenure , balance , products_number , credit_card , active_member , estimated_salary , churn in zip (data ['customer_id'], data ['credit_score'], data ['country'], data ['gender'], data ['age'], data ['tenure'], data ['balance'], data ['products_number'], data ['credit_card'], data ['active_member'], data ['estimated_salary'], data ['churn']):
	sql = "INSERT INTO banking_customer_churn(customer_id , credit_score , country , gender , age , tenure , balance , products_number , credit_card , active_member , estimated_salary , churn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (customer_id , credit_score , country , gender , age , tenure , balance , products_number , credit_card , active_member , estimated_salary , churn)
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
