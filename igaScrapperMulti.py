import asyncio
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


async def fetch_html(url):
    # Set up headless browsing
    options = Options()
    options.headless = True

    # Set up Chrome driver (adjust path based on your system)
    driver = webdriver.Chrome(options=options)

    # Open the webpage
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Get the page source (HTML)
    html = driver.page_source

    # Close the browser
    driver.quit()

    # Return the HTML
    return html


async def extract_links_from_page(my_url):
    html = await fetch_html(my_url)
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_='item-product js-product js-equalized js-addtolist-container js-ga')

    my_links = []
    for div in divs:
        data_product = div['data-product']
        product_url = data_product.split("'ProductUrl':'")[1].split("',")[0]
        my_links.append(product_url)

    return my_links


async def main():
    my_url = 'https://example.com'  # Replace with your desired URL

    links = await extract_links_from_page(my_url)
    print(links)

asyncio.run(main())
