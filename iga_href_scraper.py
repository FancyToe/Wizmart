from htmlFetcher import fetch_html
from bs4 import BeautifulSoup


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


base_url = "https://www.iga.net/fr/epicerie_en_ligne/parcourir?page="
page_number = 1
all_links = []

while True:
    url = f"{base_url}{page_number}&pageSize=200"
    print(url)
    links = extract_links_from_page(url)
    if not links:
        break
    page_number += 1
    all_links.extend(links)

with open('links.txt', 'w') as file:
    for link in all_links:
        file.write(link + '\n')
