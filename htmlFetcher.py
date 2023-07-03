from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# takes an url and returns HTML source code
def fetch_html(url):
    # Set up headless browsing
    options = Options()
    options.headless = True

    # Set up Chrome driver (adjust path based on your system)
    driver = webdriver.Chrome(options=options)

    # Open the webpage
    driver.get(url)

    # Get the page source (HTML)
    html = driver.page_source

    # Close the browser
    driver.quit()

    # Return the HTML
    return html
