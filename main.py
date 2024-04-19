# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup
# import time

# import csv

# def get_website_title(url):

#   # Specify the path to your WebDriver executable
#   driver_path = 'C:/Users/publi/Desktop/chromedriver.exe'  # Change this to the path of your WebDriver
  
#   # Initialize the WebDriver (this example uses Chrome)
#   service = Service(executable_path=driver_path)
#   options = webdriver.ChromeOptions()
#   options.add_argument('--headless')  # Enable headless mode for no GUI
#   driver = webdriver.Chrome(service=service, options=options)
    
#   try:
#     # Open the website
#     driver.get(url)
#     time.sleep(2)  # Wait for the page to load
    
#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, 'html.parser')

#     # Find the table with the aria-label attribute set to 'Live Carbon Prices'
#     table = soup.find('table', {'aria-label': 'Live Carbon Prices'})
    
#     # Get the body from the table
#     tbody = table.find('tbody')
      
#     # Iterate through each tr within the tbody
#     for row in tbody.find_all('tr'):
            
#         # Skip the header rows
#         if row.find('td').text == 'Compliance Markets' or row.find('td').text == 'Voluntary Markets':
#           continue
        
#         # Extract the data from the row
#         market = row.find_all('td')[0].text.strip()
#         price = row.find_all('td')[1].text.strip()
#         change = row.find_all('td')[2].text.strip()
#         ytd = row.find_all('td')[3].text.strip()
 
#         # Print the data
#         print(f'{market}: {price}')

#   finally:
#     driver.quit()  # Make sure to quit the driver to free resources

# # Start the script
# url = 'https://carboncredits.com/carbon-prices-today/'
# get_website_title(url)


import pandas as pd
from ecom.models import Product

def populate_database():
  df = pd.read_csv('positive.csv')
  for _, row in df.iterrows():
    row = row.to_dict()
    project_id = row['project_id']
    image_url = row['Project Images']
    product = Product.objects.get(project_id=project_id)
    product.image_url = image_url
    product.save()