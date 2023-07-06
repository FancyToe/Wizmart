from htmlFetcher import fetch_html
from bs4 import BeautifulSoup
from multiprocessing import Pool


def extract_links_from_page(page_number):
    base_url = "https://www.iga.net/fr/epicerie_en_ligne/parcourir?page="
    url = f"{base_url}{page_number}&pageSize=200"
    print(url)

    html = fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.find_all('div', class_='item-product js-product js-equalized js-addtolist-container js-ga')

    my_data = []
    for div in divs:
        data_product = div['data-product']
        my_data.append(data_product)

    return my_data


if __name__ == '__main__':
    num_pages = 10  # Number of pages to process
    pool = Pool(processes=10)  # Number of processes to run in parallel

    all_data = []
    for links in pool.map(extract_links_from_page, range(1, num_pages+1)):
        all_data.extend(links)

    with open('igaGridData.txt', 'w', encoding="UTF-8") as file:
        for data in all_data:
            file.write(data + '\n')
