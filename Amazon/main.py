import requests
from bs4 import BeautifulSoup

def search_amazon(query):
    url = f"https://www.amazon.com/s?k={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("span", {"class": "a-text-normal"})
    for result in results[:5]:  # Print first 5 results
        print(result.text)

# Example usage
query = "laptop"
search_amazon(query)