from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json

my_data = []  # List to store scraped data

options = Options()
options.add_argument('--headless')  # Configure Selenium to run in headless mode (without displaying a browser window)
driver = webdriver.Chrome(options=options)  # Create a Chrome WebDriver object

page_number = 1  # Initial page number
base_url = "https://www.iga.net/fr/epicerie_en_ligne/parcourir?page="  # Base URL

while True:
    url = f"{base_url}{page_number}&pageSize=400"  # Construct the URL for the current page number and page size
    print(url)  # Print the URL for debugging purposes

    driver.get(url)  # Navigate to the URL
    html = driver.page_source  # Get the page source HTML from the WebDriver
    soup = BeautifulSoup(html, 'html.parser')  # Create a BeautifulSoup object from the HTML

    divs = soup.find_all('div', class_='item-product js-product js-equalized js-addtolist-container js-ga')  # Find all div elements with the specified class name that contain the product data

    if not divs:  # Check if there are no more products on the page, and if so, break out of the loop
        break

    for div in divs:  # Iterate over each div element
        data_product_str = div['data-product'].replace("'", '"')
        data_product = json.loads(data_product_str)
        if not div.find('div', class_="text--small"):
            data_product["RelativePrice"] = "NULL"
        else:
            relative_price = div.find('div', class_="text--small").text.strip()
            data_product["RelativePrice"] = relative_price.replace('\n', '')
        my_data.append(data_product)  # Append the data to the my_data list

    page_number += 45  # Increment the page number for the next iteration

# End of the while loop

with open('product_data.json', 'w', encoding='utf-8') as file:
    json.dump(my_data, file, ensure_ascii=False)
