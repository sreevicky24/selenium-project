#importing libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

#10 states links
state_links=["https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/astc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile",
             "https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile"
]

# # Open the browser
# driver = webdriver.Chrome()

# # Load the webpage
# driver.get("https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile")

# wait = WebDriverWait(driver, 20)

# # Retrieve bus links and routes
# def Kerala_link_route(path):   
#     global wait  # Declare wait as global
#     LINKS_KERALA = []
#     ROUTE_KERALA = []
    
#     # Loop through a maximum of 10 pages
#     for page_number in range(1, 11):  # Limit scraping to 10 pages
#         # Wait until the route elements are present
#         wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

#         # Find all route elements on the current page
#         paths = driver.find_elements(By.XPATH, path)
        
#         print(f"Found {len(paths)} routes on page {page_number}.")  
        
#         # Extract links and route names
#         for link in paths:
#             d = link.get_attribute("href")
#             LINKS_KERALA.append(d)
#             ROUTE_KERALA.append(link.text)

#         # Attempt to navigate to the next page
#         if page_number < 10:  # Check to ensure we don't exceed 10 pages
#             try:
#                 pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

#                 # Find the active page number element
#                 active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

#                 # Find the next page number element
#                 next_page_number = int(active_page_number.text) + 1

#                 # Find the next page button element
#                 next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

#                 # Click the next page button
#                 driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
#                 time.sleep(10)  # Wait for the page to load
#                 next_page_button.click()
#                 print('Successfully navigated to the next page.')

#             except NoSuchElementException:
#                 print(f"No next page button found for page {next_page_number}. Exiting loop.")
#                 break

#             except TimeoutException:
#                 print(f'Failed to load page {page_number + 1}')

#         wait = WebDriverWait(driver, 20)

#     return LINKS_KERALA, ROUTE_KERALA


# # Retrieve data
# LINKS_KERALA, ROUTE_KERALA = Kerala_link_route("//a[@class='route']")

# # Create DataFrame
# df_kerala = pd.DataFrame({"Route_name": ROUTE_KERALA, "Route_link": LINKS_KERALA})

# # Print DataFrame 
# print(df_kerala)

# # Change DataFrame to CSV
# path = "D:\\selenium project\\df_kerala.csv"
# df_kerala.to_csv(path, index=False)

# # Close the driver
# driver.quit()



# # #ANDHRA


# # Open the browser
# driver = webdriver.Chrome()

# # Load the webpage
# driver.get("https://www.redbus.in/online-booking/apsrtc/?utm_source=rtchometile")

# wait = WebDriverWait(driver, 20)

# # Retrieve bus links and routes
# def andhra_link_route(path):   
#     global wait  # Declare wait as global
#     LINKS_andhra = []
#     ROUTE_andhra = []
    
#     # Loop through a maximum of 10 pages
#     for page_number in range(1, 11):  # Limit scraping to 10 pages
#         # Wait until the route elements are present
#         wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

#         # Find all route elements on the current page
#         paths = driver.find_elements(By.XPATH, path)
        
#         print(f"Found {len(paths)} routes on page {page_number}.")  
        
#         # Extract links and route names
#         for link in paths:
#             d = link.get_attribute("href")
#             LINKS_andhra.append(d)
#             ROUTE_andhra.append(link.text)

#         # Attempt to navigate to the next page
#         if page_number < 10:  # Check to ensure we don't exceed 10 pages
#             try:
#                 pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

#                 # Find the active page number element
#                 active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

#                 # Find the next page number element
#                 next_page_number = int(active_page_number.text) + 1

#                 # Find the next page button element
#                 next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

#                 # Click the next page button
#                 driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
#                 time.sleep(10)  # Wait for the page to load
#                 next_page_button.click()
#                 print('Successfully navigated to the next page.')

#             except NoSuchElementException:
#                 print(f"No next page button found for page {next_page_number}. Exiting loop.")
#                 break

#             except TimeoutException:
#                 print(f'Failed to load page {page_number + 1}')

#         wait = WebDriverWait(driver, 20)

#     return LINKS_andhra, ROUTE_andhra


# # Retrieve data
# LINKS_andhra, ROUTE_andhra = andhra_link_route("//a[@class='route']")

# # Create DataFrame
# df_andhra = pd.DataFrame({"Route_name": ROUTE_andhra, "Route_link": LINKS_andhra})

# # Print DataFrame 
# print(df_andhra)

# # Change DataFrame to CSV
# path ="D:\\selenium project\\df_andhra.csv"   
# df_andhra.to_csv(path, index=False)

# # Close the driver
# driver.quit()

# # #TELENGANA


# # Open the browser
# driver = webdriver.Chrome()

# # Load the webpage
# driver.get("https://www.redbus.in/online-booking/tsrtc/?utm_source=rtchometile")

# wait = WebDriverWait(driver, 20)

# # Retrieve bus links and routes
# def telengana_link_route(path):   
#     global wait  # Declare wait as global
#     LINKS_telengana = []
#     ROUTE_telengana = []
    
#     # Loop through a maximum of 10 pages
#     for page_number in range(1, 11):  # Limit scraping to 10 pages
#         # Wait until the route elements are present
#         wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

#         # Find all route elements on the current page
#         paths = driver.find_elements(By.XPATH, path)
        
#         print(f"Found {len(paths)} routes on page {page_number}.")  
        
#         # Extract links and route names
#         for link in paths:
#             d = link.get_attribute("href")
#             LINKS_telengana.append(d)
#             ROUTE_telengana.append(link.text)

#         # Attempt to navigate to the next page
#         if page_number < 10:  # Check to ensure we don't exceed 10 pages
#             try:
#                 pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

#                 # Find the active page number element
#                 active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

#                 # Find the next page number element
#                 next_page_number = int(active_page_number.text) + 1

#                 # Find the next page button element
#                 next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

#                 # Click the next page button
#                 driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
#                 time.sleep(10)  # Wait for the page to load
#                 next_page_button.click()
#                 print('Successfully navigated to the next page.')

#             except NoSuchElementException:
#                 print(f"No next page button found for page {next_page_number}. Exiting loop.")
#                 break

#             except TimeoutException:
#                 print(f'Failed to load page {page_number + 1}')

#         wait = WebDriverWait(driver, 20)

#     return LINKS_telengana, ROUTE_telengana


# # Retrieve data
# LINKS_telengana, ROUTE_telengana = telengana_link_route("//a[@class='route']")

# # Create DataFrame
# df_telengana = pd.DataFrame({"Route_name": ROUTE_telengana, "Route_link": LINKS_telengana})

# # Print DataFrame 
# print(df_telengana)

# # Change DataFrame to CSV
# path = "D:\\selenium project\\df_telengana.csv"   
# df_telengana.to_csv(path, index=False)

# # Close the driver
# driver.quit()


# #GOA


# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/ktcl/?utm_source=rtchometile")

wait = WebDriverWait(driver, 20)

# Retrieve bus links and routes
def goa_link_route(path):   
    global wait  # Declare wait as global
    LINKS_goa = []
    ROUTE_goa = []
    
    # Loop through a maximum of 10 pages
    for page_number in range(1, 11):  # Limit scraping to 10 pages
        # Wait until the route elements are present
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

        # Find all route elements on the current page
        paths = driver.find_elements(By.XPATH, path)
        
        print(f"Found {len(paths)} routes on page {page_number}.")  
        
        # Extract links and route names
        for link in paths:
            d = link.get_attribute("href")
            LINKS_goa.append(d)
            ROUTE_goa.append(link.text)

        # Attempt to navigate to the next page
        if page_number < 10:  # Check to ensure we don't exceed 10 pages
            try:
                pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

                # Find the active page number element
                active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

                # Find the next page number element
                next_page_number = int(active_page_number.text) + 1

                # Find the next page button element
                next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

                # Click the next page button
                driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
                time.sleep(10)  # Wait for the page to load
                next_page_button.click()
                print('Successfully navigated to the next page.')

            except NoSuchElementException:
                print(f"No next page button found for page {next_page_number}. Exiting loop.")
                break

            except TimeoutException:
                print(f'Failed to load page {page_number + 1}')

        wait = WebDriverWait(driver, 20)

    return LINKS_goa, ROUTE_goa


# Retrieve data
LINKS_goa, ROUTE_goa = goa_link_route("//a[@class='route']")

# Create DataFrame
df_goa = pd.DataFrame({"Route_name": ROUTE_goa, "Route_link": LINKS_goa})

# Print DataFrame 
print(df_goa)

# Change DataFrame to CSV
path = "D:\\selenium project\\df_goa.csv"
df_goa.to_csv(path, index=False)

# Close the driver
driver.quit()


# #RAJASTHAN


# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/rsrtc/?utm_source=rtchometile")

wait = WebDriverWait(driver, 20)

# Retrieve bus links and routes
def rajasthan_link_route(path):   
    global wait  # Declare wait as global
    LINKS_rajasthan = []
    ROUTE_rajasthan = []
    
    # Loop through a maximum of 10 pages
    for page_number in range(1, 11):  # Limit scraping to 10 pages
        # Wait until the route elements are present
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

        # Find all route elements on the current page
        paths = driver.find_elements(By.XPATH, path)
        
        print(f"Found {len(paths)} routes on page {page_number}.")  
        
        # Extract links and route names
        for link in paths:
            d = link.get_attribute("href")
            LINKS_rajasthan.append(d)
            ROUTE_rajasthan.append(link.text)

        # Attempt to navigate to the next page
        if page_number < 10:  # Check to ensure we don't exceed 10 pages
            try:
                pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

                # Find the active page number element
                active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

                # Find the next page number element
                next_page_number = int(active_page_number.text) + 1

                # Find the next page button element
                next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

                # Click the next page button
                driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
                time.sleep(10)  # Wait for the page to load
                next_page_button.click()
                print('Successfully navigated to the next page.')

            except NoSuchElementException:
                print(f"No next page button found for page {next_page_number}. Exiting loop.")
                break

            except TimeoutException:
                print(f'Failed to load page {page_number + 1}')

        wait = WebDriverWait(driver, 20)

    return LINKS_rajasthan, ROUTE_rajasthan


# Retrieve data
LINKS_rajasthan, ROUTE_rajasthan = rajasthan_link_route("//a[@class='route']")

# Create DataFrame
df_rajasthan = pd.DataFrame({"Route_name": ROUTE_rajasthan, "Route_link": LINKS_rajasthan})

# Print DataFrame 
print(df_rajasthan)

# Change DataFrame to CSV
path = "D:\\selenium project\\df_rajasthan.csv"
df_rajasthan.to_csv(path, index=False)

# Close the driver
driver.quit()



# #SOUTHBENGAL


# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/south-bengal-state-transport-corporation-sbstc/?utm_source=rtchometile")

wait = WebDriverWait(driver, 20)

# Retrieve bus links and routes
def sbengal_link_route(path):   
    global wait  # Declare wait as global
    LINKS_sbengal = []
    ROUTE_sbengal = []
    
    # Loop through a maximum of 10 pages
    for page_number in range(1, 11):  # Limit scraping to 10 pages
        # Wait until the route elements are present
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

        # Find all route elements on the current page
        paths = driver.find_elements(By.XPATH, path)
        
        print(f"Found {len(paths)} routes on page {page_number}.")  
        
        # Extract links and route names
        for link in paths:
            d = link.get_attribute("href")
            LINKS_sbengal.append(d)
            ROUTE_sbengal.append(link.text)

        # Attempt to navigate to the next page
        if page_number < 10:  # Check to ensure we don't exceed 10 pages
            try:
                pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

                # Find the active page number element
                active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

                # Find the next page number element
                next_page_number = int(active_page_number.text) + 1

                # Find the next page button element
                next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

                # Click the next page button
                driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
                time.sleep(10)  # Wait for the page to load
                next_page_button.click()
                print('Successfully navigated to the next page.')

            except NoSuchElementException:
                print(f"No next page button found for page {next_page_number}. Exiting loop.")
                break

            except TimeoutException:
                print(f'Failed to load page {page_number + 1}')

        wait = WebDriverWait(driver, 20)

    return LINKS_sbengal, ROUTE_sbengal


# Retrieve data
LINKS_sbengal, ROUTE_sbengal = sbengal_link_route("//a[@class='route']")

# Create DataFrame
df_sbengal = pd.DataFrame({"Route_name": ROUTE_sbengal, "Route_link": LINKS_sbengal})

# Print DataFrame 
print(df_sbengal)

# Change DataFrame to CSV
path = "D:\\selenium project\\df_sbengal.csv"
df_sbengal.to_csv(path, index=False)

# Close the driver
driver.quit()



# #HARYANA


# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/hrtc/?utm_source=rtchometile")

wait = WebDriverWait(driver, 20)

# Retrieve bus links and routes
def haryana_link_route(path):   
    global wait  # Declare wait as global
    LINKS_haryana = []
    ROUTE_haryana = []
    
    # Loop through a maximum of 10 pages
    for page_number in range(1, 11):  # Limit scraping to 10 pages
        # Wait until the route elements are present
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

        # Find all route elements on the current page
        paths = driver.find_elements(By.XPATH, path)
        
        print(f"Found {len(paths)} routes on page {page_number}.")  
        
        # Extract links and route names
        for link in paths:
            d = link.get_attribute("href")
            LINKS_haryana.append(d)
            ROUTE_haryana.append(link.text)

        # Attempt to navigate to the next page
        if page_number < 10:  # Check to ensure we don't exceed 10 pages
            try:
                pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

                # Find the active page number element
                active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

                # Find the next page number element
                next_page_number = int(active_page_number.text) + 1

                # Find the next page button element
                next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

                # Click the next page button
                driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
                time.sleep(10)  # Wait for the page to load
                next_page_button.click()
                print('Successfully navigated to the next page.')

            except NoSuchElementException:
                print(f"No next page button found for page {next_page_number}. Exiting loop.")
                break

            except TimeoutException:
                print(f'Failed to load page {page_number + 1}')

        wait = WebDriverWait(driver, 20)

    return LINKS_haryana, ROUTE_haryana


# Retrieve data
LINKS_haryana, ROUTE_haryana = haryana_link_route("//a[@class='route']")

# Create DataFrame
df_haryana = pd.DataFrame({"Route_name": ROUTE_haryana, "Route_link": LINKS_haryana})

# Print DataFrame 
print(df_haryana)

# Change DataFrame to CSV
path = "D:\\selenium project\\df_haryana.csv"
df_haryana.to_csv(path, index=False)

# Close the driver
driver.quit()


# #ASSAM


# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/astc/?utm_source=rtchometile")

wait = WebDriverWait(driver, 20)

# Retrieve bus links and routes
def assam_link_route(path):   
    global wait  # Declare wait as global
    LINKS_assam = []
    ROUTE_assam = []
    
    # Loop through a maximum of 10 pages
    for page_number in range(1, 11):  # Limit scraping to 10 pages
        # Wait until the route elements are present
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

        # Find all route elements on the current page
        paths = driver.find_elements(By.XPATH, path)
        
        print(f"Found {len(paths)} routes on page {page_number}.")  
        
        # Extract links and route names
        for link in paths:
            d = link.get_attribute("href")
            LINKS_assam.append(d)
            ROUTE_assam.append(link.text)

        # Attempt to navigate to the next page
        if page_number < 10:  # Check to ensure we don't exceed 10 pages
            try:
                pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

                # Find the active page number element
                active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

                # Find the next page number element
                next_page_number = int(active_page_number.text) + 1

                # Find the next page button element
                next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

                # Click the next page button
                driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
                time.sleep(10)  # Wait for the page to load
                next_page_button.click()
                print('Successfully navigated to the next page.')

            except NoSuchElementException:
                print(f"No next page button found for page {next_page_number}. Exiting loop.")
                break

            except TimeoutException:
                print(f'Failed to load page {page_number + 1}')

        wait = WebDriverWait(driver, 20)

    return LINKS_assam, ROUTE_assam


# Retrieve data
LINKS_assam, ROUTE_assam = assam_link_route("//a[@class='route']")

# Create DataFrame
df_assam = pd.DataFrame({"Route_name": ROUTE_assam, "Route_link": LINKS_assam})

# Print DataFrame 
print(df_assam)

# Change DataFrame to CSV
path = "D:\\selenium project\\df_assam.csv"
df_assam.to_csv(path, index=False)

# Close the driver
driver.quit()



# #UTTAR PRADESH


# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/uttar-pradesh-state-road-transport-corporation-upsrtc/?utm_source=rtchometile")

wait = WebDriverWait(driver, 20)

# Retrieve bus links and routes
def up_link_route(path):   
    global wait  # Declare wait as global
    LINKS_up = []
    ROUTE_up = []
    
    # Loop through a maximum of 10 pages
    for page_number in range(1, 11):  # Limit scraping to 10 pages
        # Wait until the route elements are present
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

        # Find all route elements on the current page
        paths = driver.find_elements(By.XPATH, path)
        
        print(f"Found {len(paths)} routes on page {page_number}.")  
        
        # Extract links and route names
        for link in paths:
            d = link.get_attribute("href")
            LINKS_up.append(d)
            ROUTE_up.append(link.text)

        # Attempt to navigate to the next page
        if page_number < 10:  # Check to ensure we don't exceed 10 pages
            try:
                pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

                # Find the active page number element
                active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

                # Find the next page number element
                next_page_number = int(active_page_number.text) + 1

                # Find the next page button element
                next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

                # Click the next page button
                driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
                time.sleep(10)  # Wait for the page to load
                next_page_button.click()
                print('Successfully navigated to the next page.')

            except NoSuchElementException:
                print(f"No next page button found for page {next_page_number}. Exiting loop.")
                break

            except TimeoutException:
                print(f'Failed to load page {page_number + 1}')

        wait = WebDriverWait(driver, 20)

    return LINKS_up, ROUTE_up


# Retrieve data
LINKS_up, ROUTE_up = up_link_route("//a[@class='route']")

# Create DataFrame
df_up = pd.DataFrame({"Route_name": ROUTE_up, "Route_link": LINKS_up})

# Print DataFrame 
print(df_up)

# Change DataFrame to CSV
path = "D:\\selenium project\\df_up.csv"  
df_up.to_csv(path, index=False)

# Close the driver
driver.quit()


#WEST BENGAL


# Open the browser
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://www.redbus.in/online-booking/wbtc-ctc/?utm_source=rtchometile")

wait = WebDriverWait(driver, 20)

# Retrieve bus links and routes
def westbengal_link_route(path):   
    global wait  # Declare wait as global
    LINKS_westbengal = []
    ROUTE_westbengal = []
    
    # Loop through a maximum of 10 pages
    for page_number in range(1, 11):  # Limit scraping to 10 pages
        # Wait until the route elements are present
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='route']")))

        # Find all route elements on the current page
        paths = driver.find_elements(By.XPATH, path)
        
        print(f"Found {len(paths)} routes on page {page_number}.")  
        
        # Extract links and route names
        for link in paths:
            d = link.get_attribute("href")
            LINKS_westbengal.append(d)
            ROUTE_westbengal.append(link.text)

        # Attempt to navigate to the next page
        if page_number < 10:  # Check to ensure we don't exceed 10 pages
            try:
                pg_container = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="D117_main D117_container"]')))

                # Find the active page number element
                active_page_number = pg_container.find_element(By.XPATH, '//div[contains(@class, "DC_117_pageTabs DC_117_pageActive")]')

                # Find the next page number element
                next_page_number = int(active_page_number.text) + 1

                # Find the next page button element
                next_page_button = pg_container.find_element(By.XPATH, f'//div[contains(@class, "DC_117_pageTabs") and text()="{next_page_number}"]')

                # Click the next page button
                driver.execute_script("arguments[0].scrollIntoView();", next_page_button)
                time.sleep(10)  # Wait for the page to load
                next_page_button.click()
                print('Successfully navigated to the next page.')

            except NoSuchElementException:
                print(f"No next page button found for page {next_page_number}. Exiting loop.")
                break

            except TimeoutException:
                print(f'Failed to load page {page_number + 1}')

        wait = WebDriverWait(driver, 20)

    return LINKS_westbengal, ROUTE_westbengal


# Retrieve data
LINKS_westbengal, ROUTE_westbengal = westbengal_link_route("//a[@class='route']")

# Create DataFrame
df_westbengal = pd.DataFrame({"Route_name": ROUTE_westbengal, "Route_link": LINKS_westbengal})

#Print DataFrame 
print(df_westbengal)

#Change DataFrame to CSV
path = "D:\\selenium project\\df_westbengal.csv"
df_westbengal.to_csv(path, index=False)

#Close the driver
driver.quit()


