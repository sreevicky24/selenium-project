# Importing libraries
import pandas as pd
import mysql.connector
import numpy as np

# CSV to dataframe
df_buses_kerala = pd.read_csv("df_buses_kerala.csv")
df_buses_andhra = pd.read_csv("df_buses_andhra.csv")
df_buses_telengana = pd.read_csv("df_buses_telengana.csv")
df_buses_goa = pd.read_csv("df_buses_goa.csv")
df_buses_rajasthan = pd.read_csv("df_buses_rajasthan.csv")
df_buses_sbengal = pd.read_csv("df_buses_sbengal.csv")
df_buses_haryana = pd.read_csv("df_buses_haryana.csv")
df_buses_assam = pd.read_csv("df_buses_assam.csv")
df_buses_up = pd.read_csv("df_buses_up.csv")
df_buses_wb = pd.read_csv("df_buses_wb.csv")

Final_df = pd.concat([df_buses_kerala,
           df_buses_andhra,
           df_buses_telengana,
           df_buses_goa,
           df_buses_rajasthan,
           df_buses_sbengal,
           df_buses_haryana,
           df_buses_assam,
           df_buses_up,
           df_buses_wb],
           ignore_index=True)

# Data about the data
Final_df.info()

# Convert prices to numeric
Final_df["Price"] = Final_df["Price"].str.replace("INR", "")
Final_df["Price"] = Final_df["Price"].astype(float)
Final_df["Price"].fillna(0)

# Convert Ratings to numeric
Final_df["Ratings"] = Final_df["Ratings"].str.replace("New", "")
Final_df["Ratings"] = Final_df["Ratings"].str.strip()
Final_df["Ratings"] = Final_df["Ratings"].str.split().str[0]
Final_df["Ratings"] = pd.to_numeric(Final_df["Ratings"], errors='coerce')
Final_df["Ratings"].fillna(0, inplace=True)

# Info after the data type change
Final_df.info()

Final_df = Final_df[Final_df["Price"] <= 7000]

Final_df['Seats_Available'].fillna('NA', inplace=True)

# Replacing the nan value
Final_df = Final_df.replace({np.nan: None})

# Change dataframe to csv
path = r"D:\\selenium project\Final_busdetails_df.csv"
Final_df.to_csv(path, index=False)

# SQL connection
conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
my_cursor = conn.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS RED_BUS_DETAILS")

# Table Creation
my_cursor.execute('''CREATE TABLE IF NOT EXISTS bus_details(
  ID INT AUTO_INCREMENT PRIMARY KEY,
  Bus_name VARCHAR(255) NOT NULL,
  Bus_type VARCHAR(255) NOT NULL,
  Start_time VARCHAR(255) NOT NULL,
  End_time VARCHAR(255) NOT NULL,
  Total_duration VARCHAR(255) NOT NULL,
  Price FLOAT NULL,
  Seats_Available VARCHAR(255) NOT NULL,
  Ratings Float NULL,
  Route_link VARCHAR(255) NULL,
  Route_name VARCHAR(255) NULL
)''')
print("Table Created successfully")


Final_df.dropna(subset=['Bus_type'], inplace=True)


# SQL query to insert data into bus_details table
insert_query = '''INSERT INTO bus_details(
  Bus_name,
  Bus_type,
  Start_time,
  End_time,
  Total_duration,
  Price,
  Seats_Available,
  Ratings,
  Route_link,
  Route_name)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
data = Final_df.values.tolist()

my_cursor.executemany(insert_query, data)

conn.commit()

print("Values insertedsuccessfully")