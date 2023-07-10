from bs4 import BeautifulSoup


def write_html(my_element, my_file_name):
    page_element_html = str(my_element)
    div_soup = BeautifulSoup(page_element_html, 'html.parser')
    div_html = div_soup.prettify()
    file_path = "html_code.txt"
    with open(file_path, 'w', encoding='utf-8') as my_file_name:
        my_file_name.write(div_html)
