# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time
 
# kerala bus
lists_k=[]
df_kerala=pd.read_csv("df_kerala.csv")
for i,r in df_kerala.iterrows():
    lists_k.append(r["Route_name"])
 
#Andhra bus
lists_A=[]
df_andhra=pd.read_csv("df_andhra.csv")
for i,r in df_andhra.iterrows():
    lists_A.append(r["Route_name"])
 
#Telungana bus
lists_T=[]
df_telengana=pd.read_csv("df_telengana.csv")
for i,r in df_telengana.iterrows():
    lists_T.append(r["Route_name"])
 
#Goa bus
lists_g=[]
df_goa=pd.read_csv("df_goa.csv")
for i,r in df_goa.iterrows():
    lists_g.append(r["Route_name"])
 
#Rajastan bus
lists_R=[]
df_rajasthan=pd.read_csv("df_rajasthan.csv")
for i,r in df_rajasthan.iterrows():
    lists_R.append(r["Route_name"])
 
 
# South bengal bus
lists_SB=[]
df_sbengal=pd.read_csv("df_sbengal.csv")
for i,r in df_sbengal.iterrows():
    lists_SB.append(r["Route_name"])
 
# Haryana bus
lists_H=[]
df_haryana=pd.read_csv("df_haryana.csv")
for i,r in df_haryana.iterrows():
    lists_H.append(r["Route_name"])
 
#Assam bus
lists_AS=[]
df_assam=pd.read_csv("df_assam.csv")
for i,r in df_assam.iterrows():
    lists_AS.append(r["Route_name"])
 
#UP bus
lists_UP=[]
df_up=pd.read_csv("df_up.csv")
for i,r in df_up.iterrows():
    lists_UP.append(r["Route_name"])
 
#West bengal bus
lists_WB=[]
df_wb=pd.read_csv("df_westbengal.csv")
for i,r in df_wb.iterrows():
    lists_WB.append(r["Route_name"])
 
#setting up streamlit page
slt.set_page_config(layout="wide")
 
web=option_menu(menu_title="SRV Bus Booking",
                options=[#"Home",
                "States and Routes"],
                icons=[#"house",
                "info-circle"],
                orientation="horizontal"
                )
# # Home page setting
# if web=="Home":
#     slt.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
#     slt.subheader(":blue[Domain:]  Transportation")
#     slt.subheader(":blue[Ojective:] ")
#     slt.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
#     slt.subheader(":blue[Overview:]")
#     slt.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
#     slt.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
#                     Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
#     slt.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
#                     and the data was efficiently inserted into relevant tables for storage and retrieval.''')
#     slt.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
#     slt.subheader(":blue[Skill-take:]")
#     slt.markdown("Selenium, Python, Pandas, MySQL,mysql-connector-python, Streamlit.")
#     slt.subheader(":blue[Developed-by:] MP SREE VIKNESHWARAN")
 
# States and Routes page setting
if web == "States and Routes":
    S = slt.selectbox("Lists of States", ["Kerala",
                                          "Adhra Pradesh", "Telugana", "Goa", "Rajastan",
                                          "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"
                                          ])
   
    col1,col2=slt.columns(2)
    with col1:
        select_type = slt.radio("Choose bus type", ("sleeper", "semi-sleeper", "others"))
    with col2:
        select_fare = slt.radio("Choose bus fare range", ("50-1000", "1000-2000", "2000 and above"))
   
    select_rating = slt.slider("Select minimum rating", min_value=0.0, max_value=5.0, value=3.0, step=0.1)
 
    TIME=slt.time_input("Select time")
 
    # Kerala bus fare filtering
    if S == "Kerala":
        K = slt.selectbox("List of routes",lists_k)
 
        def type_fare_and_rating(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
 
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition}
                AND Start_time>='{TIME}'
                AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
       
 
# Adhra Pradesh bus fare filtering
    if S=="Adhra Pradesh":
        A=slt.selectbox("list of routes",lists_A)
 
        def type_fare_and_rating_A(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_A(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
         
 
    # Telugana bus fare filtering
    if S=="Telugana":
        T=slt.selectbox("list of routes",lists_T)
 
        def type_fare_and_rating_T(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_T(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
 
    # Goa bus fare filtering
    if S=="Goa":
        G=slt.selectbox("list of routes",lists_g)
 
        def type_fare_and_rating_G(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{G}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_G(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
 
    # Rajastan bus fare filtering
    if S=="Rajastan":
        R=slt.selectbox("list of routes",lists_R)
 
        def type_fare_and_rating_R(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_R(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
         
 
    # South Bengal bus fare filtering      
    if S=="South Bengal":
        SB=slt.selectbox("list of routes",lists_SB)
 
        def type_fare_and_rating_SB(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{SB}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_SB(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
   
    # Haryana bus fare filtering
    if S=="Haryana":
        H=slt.selectbox("list of routes",lists_H)
 
        def type_fare_and_rating_H(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{H}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_H(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
 
 
    # Assam bus fare filtering
    if S=="Assam":
        AS=slt.selectbox("list of routes",lists_AS)
 
        def type_fare_and_rating_AS(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_AS(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
 
    # Utrra Pradesh bus fare filtering
    if S=="Uttar Pradesh":
        UP=slt.selectbox("list of routes",lists_UP)
 
        def type_fare_and_rating_UP(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{UP}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_UP(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)
 
    # West Bengal bus fare filtering
    if S=="West Bengal":
        WB=slt.selectbox("list of routes",lists_WB)
 
        def type_fare_and_rating_WB(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Vicky", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  
 
            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"
 
            query = f'''
                SELECT * FROM bus_details
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{WB}"
                AND {bus_type_condition} AND Start_time>='{TIME}' AND Ratings>= {select_rating}
                ORDER BY Price and Start_time  DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()
 
            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df
 
        df_result = type_fare_and_rating_WB(select_type, select_fare)
        slt.dataframe(df_result, use_container_width=True)