import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline - used in notebooks (google colab / jupyter) only.

import mysql.connector
from decouple import config


from preprocessing import retrun_statistics, seperate_columns_numerical_categorical

data = pd.read_csv("/home/ilaf/Desktop/EDA_Projects/screenTime/dataSource/Screentime-App-Details.csv", encoding_errors = "ignore")
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

for UsageDate, UsageTime, Notifications, TimesOpened, App in zip (data['UsageDate'], data['UsageTime'], data['Notifications'], data['TimesOpened'], data['App']):
	sql = "INSERT INTO screenData (UsageDate, UsageTime, Notifications, TimesOpened, App) VALUES (%s, %s, %s, %s, %s)"
	val = (UsageDate, UsageTime, Notifications, TimesOpened, App)
	mycursor.execute(sql, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")

