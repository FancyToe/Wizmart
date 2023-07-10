from htmlFetcher import fetch_html
from bs4 import BeautifulSoup
from multiprocessing import Pool
import json
from write_element_html import write_html


def extract_links_from_page(page_number):
    base_url = "https://www.iga.net/fr/epicerie_en_ligne/parcourir?page="
    url = f"{base_url}{page_number}&pageSize=1"
    print(url)

    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.find_all('div', class_='item-product js-product js-equalized js-addtolist-container js-ga')

    my_data = []
    for div in divs:
        write_html(div, 'html_code.txt')

        # Replace single quotes with double quotes
        data_product_str = div['data-product'].replace("'", '"')
        data_product = json.loads(data_product_str)
        data_product["Sustentation"] = "Maximus militarus junglus diffus"
        my_data.append(data_product)

    return my_data


if __name__ == '__main__':
    num_pages = 92  # Number of pages to process
    pool = Pool(processes=10)  # Number of processes to run in parallel

    all_data = []
    for links in pool.map(extract_links_from_page, range(1, num_pages+1)):
        all_data.extend(links)

    with open('igaGridData.json', 'w', encoding='UTF-8') as file:
        json.dump(all_data, file, indent=2)
