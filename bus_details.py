# importing libraries
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# #KERALA

# # read the csv file
# df=pd.read_csv("df_kerala.csv")
# df

# #retrive the bus details
# driver_kerala = webdriver.Chrome()
# Bus_names_kerala = []
# Bus_types_kerala = []
# Start_Time_kerala = []
# End_Time_kerala = []
# Ratings_kerala = []
# Total_Duration_kerala = []
# Prices_kerala = []
# Seats_Available_kerala = []
# Route_names = []
# Route_links = []

# for i,r in df.iterrows():
#     link=r["Route_link"]
#     routes=r["Route_name"]

# # Loop through each link
#     driver_kerala.get(link)
#     time.sleep(2)  

#     # Click on elements to reveal bus details
#     elements = driver_kerala.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
#     for element in elements:
#         element.click()
#         time.sleep(2)
        
#     # click elements to views bus
#     try:
#         clicks = driver_kerala.find_element(By.XPATH, "//div[@class='button']")
#         clicks.click()
#     except:
#         continue  
#     time.sleep(2)
    
#     scrolling = True
#     while scrolling:
#         old_page_source = driver_kerala.page_source
        
#         # Use ActionChains to perform a PAGE_DOWN
#         ActionChains(driver_kerala).send_keys(Keys.PAGE_DOWN).perform()
        
#         time.sleep(5)  
        
#         new_page_source = driver_kerala.page_source
        
#         if new_page_source == old_page_source:
#             scrolling = False

#     # Extract bus details
#     bus_name = driver_kerala.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
#     bus_type = driver_kerala.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
#     start_time = driver_kerala.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
#     end_time = driver_kerala.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
#     total_duration = driver_kerala.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
#     try:
#         rating = driver_kerala.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
#     except:
#         continue
#     price = driver_kerala.find_elements(By.XPATH, '//*[@class="fare d-block"]')
#     seats = driver_kerala.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

#     # Append data to respective lists
#     for bus in bus_name:
#         Bus_names_kerala.append(bus.text)
#         Route_links.append(link)
#         Route_names.append(routes)
#     for bus_type_elem in bus_type:
#         Bus_types_kerala.append(bus_type_elem.text)
#     for start_time_elem in start_time:
#         Start_Time_kerala.append(start_time_elem.text)
#     for end_time_elem in end_time:
#         End_Time_kerala.append(end_time_elem.text)
#     for total_duration_elem in total_duration:
#         Total_Duration_kerala.append(total_duration_elem.text)
#     for ratings in rating:
#         Ratings_kerala.append(ratings.text)
#     for price_elem in price:
#         Prices_kerala.append(price_elem.text)
#     for seats_elem in seats:
#         Seats_Available_kerala.append(seats_elem.text)
        
# print("Successfully Completed")

# # from list to convert data frame
# data = {
#     'Bus_name': Bus_names_kerala,
#     'Bus_type': Bus_types_kerala,
#     'Start_time': Start_Time_kerala,
#     'End_time': End_Time_kerala,
#     'Total_duration': Total_Duration_kerala,
#     'Price': Prices_kerala,
#     "Seats_Available":Seats_Available_kerala,
#     "Ratings":Ratings_kerala,
#     'Route_link': Route_links,
#     'Route_name': Route_names
# }

# df_buses_kerala = pd.DataFrame(data)
# #convert dataframe to csv
# path="D:\\selenium project\\df_buses_kerala.csv"
# df_buses_kerala.to_csv(path,index=False)

# #Andhra

# # read the csv file
# df=pd.read_csv("df_andhra.csv")
# df

# #retrive the bus details
# driver_andhra = webdriver.Chrome()
# Bus_names_andhra = []
# Bus_types_andhra = []
# Start_Time_andhra = []
# End_Time_andhra = []
# Ratings_andhra = []
# Total_Duration_andhra = []
# Prices_andhra = []
# Seats_Available_andhra = []
# Route_names = []
# Route_links = []

# for i,r in df.iterrows():
#     link=r["Route_link"]
#     routes=r["Route_name"]

# # Loop through each link
#     driver_andhra.get(link)
#     time.sleep(2)  

#     # Click on elements to reveal bus details
#     elements = driver_andhra.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
#     for element in elements:
#         element.click()
#         time.sleep(2)
        
#     # click elements to views bus
#     try:
#         clicks = driver_andhra.find_element(By.XPATH, "//div[@class='button']")
#         clicks.click()
#     except:
#         continue  
#     time.sleep(2)
    
#     scrolling = True
#     while scrolling:
#         old_page_source = driver_andhra.page_source
        
#         # Use ActionChains to perform a PAGE_DOWN
#         ActionChains(driver_andhra).send_keys(Keys.PAGE_DOWN).perform()
        
#         time.sleep(5)  
        
#         new_page_source = driver_andhra.page_source
        
#         if new_page_source == old_page_source:
#             scrolling = False

#     # Extract bus details
#     bus_name = driver_andhra.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
#     bus_type = driver_andhra.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
#     start_time = driver_andhra.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
#     end_time = driver_andhra.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
#     total_duration = driver_andhra.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
#     try:
#         rating = driver_andhra.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
#     except:
#         continue
#     price = driver_andhra.find_elements(By.XPATH, '//*[@class="fare d-block"]')
#     seats = driver_andhra.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

#     # Append data to respective lists
#     for bus in bus_name:
#         Bus_names_andhra.append(bus.text)
#         Route_links.append(link)
#         Route_names.append(routes)
#     for bus_type_elem in bus_type:
#         Bus_types_andhra.append(bus_type_elem.text)
#     for start_time_elem in start_time:
#         Start_Time_andhra.append(start_time_elem.text)
#     for end_time_elem in end_time:
#         End_Time_andhra.append(end_time_elem.text)
#     for total_duration_elem in total_duration:
#         Total_Duration_andhra.append(total_duration_elem.text)
#     for ratings in rating:
#         Ratings_andhra.append(ratings.text)
#     for price_elem in price:
#         Prices_andhra.append(price_elem.text)
#     for seats_elem in seats:
#         Seats_Available_andhra.append(seats_elem.text)
        
# print("Successfully Completed")

# # from list to convert data frame
# data = {
#     'Bus_name': Bus_names_andhra,
#     'Bus_type': Bus_types_andhra,
#     'Start_time': Start_Time_andhra,
#     'End_time': End_Time_andhra,
#     'Total_duration': Total_Duration_andhra,
#     'Price': Prices_andhra,
#     "Seats_Available":Seats_Available_andhra,
#     "Ratings":Ratings_andhra,
#     'Route_link': Route_links,
#     'Route_name': Route_names
# }

# df_buses_andhra = pd.DataFrame(data)
# #convert dataframe to csv
# path="D:\\selenium project\\df_buses_andhra.csv"
# df_buses_andhra.to_csv(path,index=False)

# #TELENGANA

# # read the csv file
# df=pd.read_csv("df_telengana.csv")
# df

# #retrive the bus details
# driver_telengana = webdriver.Chrome()
# Bus_names_telengana = []
# Bus_types_telengana = []
# Start_Time_telengana = []
# End_Time_telengana = []
# Ratings_telengana = []
# Total_Duration_telengana = []
# Prices_telengana = []
# Seats_Available_telengana = []
# Route_names = []
# Route_links = []

# for i,r in df.iterrows():
#     link=r["Route_link"]
#     routes=r["Route_name"]

# # Loop through each link
#     driver_telengana.get(link)
#     time.sleep(2)  

#     # Click on elements to reveal bus details
#     elements = driver_telengana.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
#     for element in elements:
#         element.click()
#         time.sleep(2)
        
#     # click elements to views bus
#     try:
#         clicks = driver_telengana.find_element(By.XPATH, "//div[@class='button']")
#         clicks.click()
#     except:
#         continue  
#     time.sleep(2)
    
#     scrolling = True
#     while scrolling:
#         old_page_source = driver_telengana.page_source
        
#         # Use ActionChains to perform a PAGE_DOWN
#         ActionChains(driver_telengana).send_keys(Keys.PAGE_DOWN).perform()
        
#         time.sleep(5)  
        
#         new_page_source = driver_telengana.page_source
        
#         if new_page_source == old_page_source:
#             scrolling = False

#     # Extract bus details
#     bus_name = driver_telengana.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
#     bus_type = driver_telengana.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
#     start_time = driver_telengana.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
#     end_time = driver_telengana.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
#     total_duration = driver_telengana.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
#     try:
#         rating = driver_telengana.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
#     except:
#         continue
#     price = driver_telengana.find_elements(By.XPATH, '//*[@class="fare d-block"]')
#     seats = driver_telengana.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

#     # Append data to respective lists
#     for bus in bus_name:
#         Bus_names_telengana.append(bus.text)
#         Route_links.append(link)
#         Route_names.append(routes)
#     for bus_type_elem in bus_type:
#         Bus_types_telengana.append(bus_type_elem.text)
#     for start_time_elem in start_time:
#         Start_Time_telengana.append(start_time_elem.text)
#     for end_time_elem in end_time:
#         End_Time_telengana.append(end_time_elem.text)
#     for total_duration_elem in total_duration:
#         Total_Duration_telengana.append(total_duration_elem.text)
#     for ratings in rating:
#         Ratings_telengana.append(ratings.text)
#     for price_elem in price:
#         Prices_telengana.append(price_elem.text)
#     for seats_elem in seats:
#         Seats_Available_telengana.append(seats_elem.text)
        
# print("Successfully Completed")

# # from list to convert data frame
# data = {
#     'Bus_name': Bus_names_telengana,
#     'Bus_type': Bus_types_telengana,
#     'Start_time': Start_Time_telengana,
#     'End_time': End_Time_telengana,
#     'Total_duration': Total_Duration_telengana,
#     'Price': Prices_telengana,
#     "Seats_Available":Seats_Available_telengana,
#     "Ratings":Ratings_telengana,
#     'Route_link': Route_links,
#     'Route_name': Route_names
# }

# df_buses_telengana = pd.DataFrame(data)
# #convert dataframe to csv
# path="D:\\selenium project\\df_buses_telengana.csv"
# df_buses_telengana.to_csv(path,index=False)


# #GOA

# # read the csv file
# df=pd.read_csv("df_goa.csv")
# df

# #retrive the bus details
# driver_goa = webdriver.Chrome()
# Bus_names_goa = []
# Bus_types_goa = []
# Start_Time_goa = []
# End_Time_goa = []
# Ratings_goa = []
# Total_Duration_goa = []
# Prices_goa = []
# Seats_Available_goa = []
# Route_names = []
# Route_links = []

# for i,r in df.iterrows():
#     link=r["Route_link"]
#     routes=r["Route_name"]

# # Loop through each link
#     driver_goa.get(link)
#     time.sleep(2)  

#     # Click on elements to reveal bus details
#     elements = driver_goa.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
#     for element in elements:
#         element.click()
#         time.sleep(2)
        
#     # click elements to views bus
#     try:
#         clicks = driver_goa.find_element(By.XPATH, "//div[@class='button']")
#         clicks.click()
#     except:
#         continue  
#     time.sleep(2)
    
#     scrolling = True
#     while scrolling:
#         old_page_source = driver_goa.page_source
        
#         # Use ActionChains to perform a PAGE_DOWN
#         ActionChains(driver_goa).send_keys(Keys.PAGE_DOWN).perform()
        
#         time.sleep(5)  
        
#         new_page_source = driver_goa.page_source
        
#         if new_page_source == old_page_source:
#             scrolling = False

#     # Extract bus details
#     bus_name = driver_goa.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
#     bus_type = driver_goa.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
#     start_time = driver_goa.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
#     end_time = driver_goa.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
#     total_duration = driver_goa.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
#     try:
#         rating = driver_goa.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
#     except:
#         continue
#     price = driver_goa.find_elements(By.XPATH, '//*[@class="fare d-block"]')
#     seats = driver_goa.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

#     # Append data to respective lists
#     for bus in bus_name:
#         Bus_names_goa.append(bus.text)
#         Route_links.append(link)
#         Route_names.append(routes)
#     for bus_type_elem in bus_type:
#         Bus_types_goa.append(bus_type_elem.text)
#     for start_time_elem in start_time:
#         Start_Time_goa.append(start_time_elem.text)
#     for end_time_elem in end_time:
#         End_Time_goa.append(end_time_elem.text)
#     for total_duration_elem in total_duration:
#         Total_Duration_goa.append(total_duration_elem.text)
#     for ratings in rating:
#         Ratings_goa.append(ratings.text)
#     for price_elem in price:
#         Prices_goa.append(price_elem.text)
#     for seats_elem in seats:
#         Seats_Available_goa.append(seats_elem.text)
        
# print("Successfully Completed")

# # from list to convert data frame
# data = {
#     'Bus_name': Bus_names_goa,
#     'Bus_type': Bus_types_goa,
#     'Start_time': Start_Time_goa,
#     'End_time': End_Time_goa,
#     'Total_duration': Total_Duration_goa,
#     'Price': Prices_goa,
#     "Seats_Available":Seats_Available_goa,
#     "Ratings":Ratings_goa,
#     'Route_link': Route_links,
#     'Route_name': Route_names
# }

# df_buses_goa = pd.DataFrame(data)
# #convert dataframe to csv
# path="D:\\selenium project\\df_buses_goa.csv"
# df_buses_goa.to_csv(path,index=False)


# #RAJASTHAN

# # read the csv file
# df=pd.read_csv("df_rajasthan.csv")
# df

# #retrive the bus details
# driver_rajasthan = webdriver.Chrome()
# Bus_names_rajasthan = []
# Bus_types_rajasthan = []
# Start_Time_rajasthan = []
# End_Time_rajasthan = []
# Ratings_rajasthan = []
# Total_Duration_rajasthan = []
# Prices_rajasthan = []
# Seats_Available_rajasthan = []
# Route_names = []
# Route_links = []

# for i,r in df.iterrows():
#     link=r["Route_link"]
#     routes=r["Route_name"]

# # Loop through each link
#     driver_rajasthan.get(link)
#     time.sleep(2)  

#     # Click on elements to reveal bus details
#     elements = driver_rajasthan.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
#     for element in elements:
#         element.click()
#         time.sleep(2)
        
#     # click elements to views bus
#     try:
#         clicks = driver_rajasthan.find_element(By.XPATH, "//div[@class='button']")
#         clicks.click()
#     except:
#         continue  
#     time.sleep(2)
    
#     scrolling = True
#     while scrolling:
#         old_page_source = driver_rajasthan.page_source
        
#         # Use ActionChains to perform a PAGE_DOWN
#         ActionChains(driver_rajasthan).send_keys(Keys.PAGE_DOWN).perform()
        
#         time.sleep(5)  
        
#         new_page_source = driver_rajasthan.page_source
        
#         if new_page_source == old_page_source:
#             scrolling = False

#     # Extract bus details
#     bus_name = driver_rajasthan.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
#     bus_type = driver_rajasthan.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
#     start_time = driver_rajasthan.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
#     end_time = driver_rajasthan.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
#     total_duration = driver_rajasthan.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
#     try:
#         rating = driver_rajasthan.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
#     except:
#         continue
#     price = driver_rajasthan.find_elements(By.XPATH, '//*[@class="fare d-block"]')
#     seats = driver_rajasthan.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

#     # Append data to respective lists
#     for bus in bus_name:
#         Bus_names_rajasthan.append(bus.text)
#         Route_links.append(link)
#         Route_names.append(routes)
#     for bus_type_elem in bus_type:
#         Bus_types_rajasthan.append(bus_type_elem.text)
#     for start_time_elem in start_time:
#         Start_Time_rajasthan.append(start_time_elem.text)
#     for end_time_elem in end_time:
#         End_Time_rajasthan.append(end_time_elem.text)
#     for total_duration_elem in total_duration:
#         Total_Duration_rajasthan.append(total_duration_elem.text)
#     for ratings in rating:
#         Ratings_rajasthan.append(ratings.text)
#     for price_elem in price:
#         Prices_rajasthan.append(price_elem.text)
#     for seats_elem in seats:
#         Seats_Available_rajasthan.append(seats_elem.text)
        
# print("Successfully Completed")

# # from list to convert data frame
# data = {
#     'Bus_name': Bus_names_rajasthan,
#     'Bus_type': Bus_types_rajasthan,
#     'Start_time': Start_Time_rajasthan,
#     'End_time': End_Time_rajasthan,
#     'Total_duration': Total_Duration_rajasthan,
#     'Price': Prices_rajasthan,
#     "Seats_Available":Seats_Available_rajasthan,
#     "Ratings":Ratings_rajasthan,
#     'Route_link': Route_links,
#     'Route_name': Route_names
# }

# df_buses_rajasthan = pd.DataFrame(data)
# #convert dataframe to csv
# path="D:\\selenium project\\df_buses_rajasthan.csv"
# df_buses_rajasthan.to_csv(path,index=False)


# #SOUTH BENGAL

# # read the csv file
# df=pd.read_csv("df_sbengal.csv")
# df

# #retrive the bus details
# driver_sbengal = webdriver.Chrome()
# Bus_names_sbengal = []
# Bus_types_sbengal = []
# Start_Time_sbengal = []
# End_Time_sbengal = []
# Ratings_sbengal = []
# Total_Duration_sbengal = []
# Prices_sbengal = []
# Seats_Available_sbengal = []
# Route_names = []
# Route_links = []

# for i,r in df.iterrows():
#     link=r["Route_link"]
#     routes=r["Route_name"]

# # Loop through each link
#     driver_sbengal.get(link)
#     time.sleep(2)  

#     # Click on elements to reveal bus details
#     elements = driver_sbengal.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
#     for element in elements:
#         element.click()
#         time.sleep(2)
        
#     # click elements to views bus
#     try:
#         clicks = driver_sbengal.find_element(By.XPATH, "//div[@class='button']")
#         clicks.click()
#     except:
#         continue  
#     time.sleep(2)
    
#     scrolling = True
#     while scrolling:
#         old_page_source = driver_sbengal.page_source
        
#         # Use ActionChains to perform a PAGE_DOWN
#         ActionChains(driver_sbengal).send_keys(Keys.PAGE_DOWN).perform()
        
#         time.sleep(5)  
        
#         new_page_source = driver_sbengal.page_source
        
#         if new_page_source == old_page_source:
#             scrolling = False

#     # Extract bus details
#     bus_name = driver_sbengal.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
#     bus_type = driver_sbengal.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
#     start_time = driver_sbengal.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
#     end_time = driver_sbengal.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
#     total_duration = driver_sbengal.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
#     try:
#         rating = driver_sbengal.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
#     except:
#         continue
#     price = driver_sbengal.find_elements(By.XPATH, '//*[@class="fare d-block"]')
#     seats = driver_sbengal.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

#     # Append data to respective lists
#     for bus in bus_name:
#         Bus_names_sbengal.append(bus.text)
#         Route_links.append(link)
#         Route_names.append(routes)
#     for bus_type_elem in bus_type:
#         Bus_types_sbengal.append(bus_type_elem.text)
#     for start_time_elem in start_time:
#         Start_Time_sbengal.append(start_time_elem.text)
#     for end_time_elem in end_time:
#         End_Time_sbengal.append(end_time_elem.text)
#     for total_duration_elem in total_duration:
#         Total_Duration_sbengal.append(total_duration_elem.text)
#     for ratings in rating:
#         Ratings_sbengal.append(ratings.text)
#     for price_elem in price:
#         Prices_sbengal.append(price_elem.text)
#     for seats_elem in seats:
#         Seats_Available_sbengal.append(seats_elem.text)
        
# print("Successfully Completed")

# # from list to convert data frame
# data = {
#     'Bus_name': Bus_names_sbengal,
#     'Bus_type': Bus_types_sbengal,
#     'Start_time': Start_Time_sbengal,
#     'End_time': End_Time_sbengal,
#     'Total_duration': Total_Duration_sbengal,
#     'Price': Prices_sbengal,
#     "Seats_Available":Seats_Available_sbengal,
#     "Ratings":Ratings_sbengal,
#     'Route_link': Route_links,
#     'Route_name': Route_names
# }

# df_buses_sbengal = pd.DataFrame(data)
# #convert dataframe to csv
# path="D:\\selenium project\\df_buses_sbengal.csv"
# df_buses_sbengal.to_csv(path,index=False)


# #HARYANA

# # read the csv file
# df=pd.read_csv("df_haryana.csv")
# df

# #retrive the bus details
# driver_haryana = webdriver.Chrome()
# Bus_names_haryana = []
# Bus_types_haryana = []
# Start_Time_haryana = []
# End_Time_haryana = []
# Ratings_haryana = []
# Total_Duration_haryana = []
# Prices_haryana = []
# Seats_Available_haryana = []
# Route_names = []
# Route_links = []

# for i,r in df.iterrows():
#     link=r["Route_link"]
#     routes=r["Route_name"]

# # Loop through each link
#     driver_haryana.get(link)
#     time.sleep(2)  

#     # Click on elements to reveal bus details
#     elements = driver_haryana.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
#     for element in elements:
#         element.click()
#         time.sleep(2)
        
#     # click elements to views bus
#     try:
#         clicks = driver_haryana.find_element(By.XPATH, "//div[@class='button']")
#         clicks.click()
#     except:
#         continue  
#     time.sleep(2)
    
#     scrolling = True
#     while scrolling:
#         old_page_source = driver_haryana.page_source
        
#         # Use ActionChains to perform a PAGE_DOWN
#         ActionChains(driver_haryana).send_keys(Keys.PAGE_DOWN).perform()
        
#         time.sleep(5)  
        
#         new_page_source = driver_haryana.page_source
        
#         if new_page_source == old_page_source:
#             scrolling = False

#     # Extract bus details
#     bus_name = driver_haryana.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
#     bus_type = driver_haryana.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
#     start_time = driver_haryana.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
#     end_time = driver_haryana.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
#     total_duration = driver_haryana.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
#     try:
#         rating = driver_haryana.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
#     except:
#         continue
#     price = driver_haryana.find_elements(By.XPATH, '//*[@class="fare d-block"]')
#     seats = driver_haryana.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

#     # Append data to respective lists
#     for bus in bus_name:
#         Bus_names_haryana.append(bus.text)
#         Route_links.append(link)
#         Route_names.append(routes)
#     for bus_type_elem in bus_type:
#         Bus_types_haryana.append(bus_type_elem.text)
#     for start_time_elem in start_time:
#         Start_Time_haryana.append(start_time_elem.text)
#     for end_time_elem in end_time:
#         End_Time_haryana.append(end_time_elem.text)
#     for total_duration_elem in total_duration:
#         Total_Duration_haryana.append(total_duration_elem.text)
#     for ratings in rating:
#         Ratings_haryana.append(ratings.text)
#     for price_elem in price:
#         Prices_haryana.append(price_elem.text)
#     for seats_elem in seats:
#         Seats_Available_haryana.append(seats_elem.text)
        
# print("Successfully Completed")

# # from list to convert data frame
# data = {
#     'Bus_name': Bus_names_haryana,
#     'Bus_type': Bus_types_haryana,
#     'Start_time': Start_Time_haryana,
#     'End_time': End_Time_haryana,
#     'Total_duration': Total_Duration_haryana,
#     'Price': Prices_haryana,
#     "Seats_Available":Seats_Available_haryana,
#     "Ratings":Ratings_haryana,
#     'Route_link': Route_links,
#     'Route_name': Route_names
# }

# df_buses_haryana = pd.DataFrame(data)
# #convert dataframe to csv
# path="D:\\selenium project\\df_buses_haryana.csv"
# df_buses_haryana.to_csv(path,index=False)


#ASSAM


# read the csv file
df=pd.read_csv("df_assam.csv")
df

#retrive the bus details
driver_assam = webdriver.Chrome()
Bus_names_assam = []
Bus_types_assam = []
Start_Time_assam = []
End_Time_assam = []
Ratings_assam = []
Total_Duration_assam = []
Prices_assam = []
Seats_Available_assam = []
Route_names = []
Route_links = []

for i,r in df.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_assam.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_assam.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
        
    # click elements to views bus
    try:
        clicks = driver_assam.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue  
    time.sleep(2)
    
    scrolling = True
    while scrolling:
        old_page_source = driver_assam.page_source
        
        # Use ActionChains to perform a PAGE_DOWN
        ActionChains(driver_assam).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_assam.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_assam.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_assam.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_assam.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_assam.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_assam.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_assam.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_assam.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_assam.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_assam.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_assam.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_assam.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_assam.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_assam.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_assam.append(ratings.text)
    for price_elem in price:
        Prices_assam.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_assam.append(seats_elem.text)
        
print("Successfully Completed")

# from list to convert data frame
data = {
    'Bus_name': Bus_names_assam,
    'Bus_type': Bus_types_assam,
    'Start_time': Start_Time_assam,
    'End_time': End_Time_assam,
    'Total_duration': Total_Duration_assam,
    'Price': Prices_assam,
    "Seats_Available":Seats_Available_assam,
    "Ratings":Ratings_assam,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_assam = pd.DataFrame(data)
#convert dataframe to csv
path="D:\\selenium project\\df_buses_assam.csv"
df_buses_assam.to_csv(path,index=False)

#UP

# read the csv file
df=pd.read_csv("df_up.csv")
df

#retrive the bus details
driver_up = webdriver.Chrome()
Bus_names_up = []
Bus_types_up = []
Start_Time_up = []
End_Time_up = []
Ratings_up = []
Total_Duration_up = []
Prices_up = []
Seats_Available_up = []
Route_names = []
Route_links = []

for i,r in df.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_up.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_up.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
        
    # click elements to views bus
    try:
        clicks = driver_up.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue  
    time.sleep(2)
    
    scrolling = True
    while scrolling:
        old_page_source = driver_up.page_source
        
        # Use ActionChains to perform a PAGE_DOWN
        ActionChains(driver_up).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_up.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_up.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_up.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_up.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_up.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_up.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_up.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_up.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_up.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_up.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_up.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_up.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_up.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_up.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_up.append(ratings.text)
    for price_elem in price:
        Prices_up.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_up.append(seats_elem.text)
        
print("Successfully Completed")

# from list to convert data frame
data = {
    'Bus_name': Bus_names_up,
    'Bus_type': Bus_types_up,
    'Start_time': Start_Time_up,
    'End_time': End_Time_up,
    'Total_duration': Total_Duration_up,
    'Price': Prices_up,
    "Seats_Available":Seats_Available_up,
    "Ratings":Ratings_up,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_up = pd.DataFrame(data)
#convert dataframe to csv
path="D:\\selenium project\\df_buses_up.csv"
df_buses_up.to_csv(path,index=False)


#WB

# read the csv file
df=pd.read_csv("df_westbengal.csv")
df

#retrive the bus details
driver_wb = webdriver.Chrome()
Bus_names_wb = []
Bus_types_wb = []
Start_Time_wb = []
End_Time_wb = []
Ratings_wb = []
Total_Duration_wb = []
Prices_wb = []
Seats_Available_wb = []
Route_names = []
Route_links = []

for i,r in df.iterrows():
    link=r["Route_link"]
    routes=r["Route_name"]

# Loop through each link
    driver_wb.get(link)
    time.sleep(2)  

    # Click on elements to reveal bus details
    elements = driver_wb.find_elements(By.XPATH, f"//a[contains(@href, '{link}')]")
    for element in elements:
        element.click()
        time.sleep(2)
        
    # click elements to views bus
    try:
        clicks = driver_wb.find_element(By.XPATH, "//div[@class='button']")
        clicks.click()
    except:
        continue  
    time.sleep(2)
    
    scrolling = True
    while scrolling:
        old_page_source = driver_wb.page_source
        
        # Use ActionChains to perform a PAGE_DOWN
        ActionChains(driver_wb).send_keys(Keys.PAGE_DOWN).perform()
        
        time.sleep(5)  
        
        new_page_source = driver_wb.page_source
        
        if new_page_source == old_page_source:
            scrolling = False

    # Extract bus details
    bus_name = driver_wb.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    bus_type = driver_wb.find_elements(By.XPATH, "//div[@class='bus-type f-12 m-top-16 l-color evBus']")
    start_time = driver_wb.find_elements(By.XPATH, "//*[@class='dp-time f-19 d-color f-bold']")
    end_time = driver_wb.find_elements(By.XPATH, "//*[@class='bp-time f-19 d-color disp-Inline']")
    total_duration = driver_wb.find_elements(By.XPATH, "//*[@class='dur l-color lh-24']")
    try:
        rating = driver_wb.find_elements(By.XPATH,"//div[@class='clearfix row-one']/div[@class='column-six p-right-10 w-10 fl']")
    except:
        continue
    price = driver_wb.find_elements(By.XPATH, '//*[@class="fare d-block"]')
    seats = driver_wb.find_elements(By.XPATH, "//div[contains(@class, 'seat-left')]")

    # Append data to respective lists
    for bus in bus_name:
        Bus_names_wb.append(bus.text)
        Route_links.append(link)
        Route_names.append(routes)
    for bus_type_elem in bus_type:
        Bus_types_wb.append(bus_type_elem.text)
    for start_time_elem in start_time:
        Start_Time_wb.append(start_time_elem.text)
    for end_time_elem in end_time:
        End_Time_wb.append(end_time_elem.text)
    for total_duration_elem in total_duration:
        Total_Duration_wb.append(total_duration_elem.text)
    for ratings in rating:
        Ratings_wb.append(ratings.text)
    for price_elem in price:
        Prices_wb.append(price_elem.text)
    for seats_elem in seats:
        Seats_Available_wb.append(seats_elem.text)
        
print("Successfully Completed")

# from list to convert data frame
data = {
    'Bus_name': Bus_names_wb,
    'Bus_type': Bus_types_wb,
    'Start_time': Start_Time_wb,
    'End_time': End_Time_wb,
    'Total_duration': Total_Duration_wb,
    'Price': Prices_wb,
    "Seats_Available":Seats_Available_wb,
    "Ratings":Ratings_wb,
    'Route_link': Route_links,
    'Route_name': Route_names
}

df_buses_wb = pd.DataFrame(data)
#convert dataframe to csv
path="D:\\selenium project\\df_buses_wb.csv"
df_buses_wb.to_csv(path,index=False)