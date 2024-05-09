import requests
from bs4 import BeautifulSoup


def fetch_data(url):
    # Send a request to the URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print("Failed to retrieve data")
        return None


def parse_data(soup):
    # Example: Find all data you need, this is just a placeholder
    data = soup.find_all('div', id='xmoApp__keyTakeAways')  # Modify this line as needed
    for item in data:
        print(item.text)  # Extract text or any other data you need


if __name__ == "__main__":
    url = 'https://www.statista.com/outlook/cmo/footwear/india'
    soup = fetch_data(url)
    if soup:
        parse_data(soup)
