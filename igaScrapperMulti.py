import concurrent.futures
from htmlFetcher import fetch_html
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_links_from_page(my_url):
    # Fetch html from url and define soup
    html = fetch_html(my_url)
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the divs with desired class name
    divs = soup.find_all('div', class_='item-product js-product js-equalized js-addtolist-container js-ga')

    # Extract ProductUrl from every element in divs
    my_links = []
    for div in divs:
        data_product = div['data-product']
        product_url = data_product.split("'ProductUrl':'")[1].split("',")[0]
        my_links.append(product_url)

    return my_links


def process_page(page_number):
    url = f"{base_url}{page_number}&pageSize=200"
    print(url)
    links = extract_links_from_page(url)
    return links


base_url = "https://www.iga.net/fr/epicerie_en_ligne/parcourir?page="
total_pages = 20
all_links = []

# Create Chrome options with headless mode
chrome_options = Options()
chrome_options.add_argument('--headless')

# Create a pool of Chrome drivers with headless option
driver_pool = [webdriver.Chrome(options=chrome_options) for _ in range(total_pages)]

# Process each page concurrently
with concurrent.futures.ThreadPoolExecutor() as executor:
    page_numbers = range(1, total_pages + 1)
    results = executor.map(process_page, page_numbers)

    # Collect the results
    for links in results:
        if not links:
            break
        all_links.extend(links)

# Close the Chrome drivers
for driver in driver_pool:
    driver.quit()

# Write links to a text file
with open('links.txt', 'w') as file:
    for link in all_links:
        file.write(link + '\n')

print("Links written to links.txt")
