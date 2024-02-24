import requests
from bs4 import BeautifulSoup

def search_amazon(product_name):
    # Define the URL for Amazon's search results page
    url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the product elements
    products = soup.find_all('div', {'class': 'sg-col-inner'})

    # Initialize a list to store the product names
    product_list = []

    # Extract product names from each product element
    for product in products:
        # Extract the product name
        product_name = product.find('span', {'class': 'a-size-medium'}).text.strip()
        
        # Add the product name to the list
        product_list.append(product_name)

    return product_list

# Example usage:
search_query = input("Enter the product name to search on Amazon: ")
products = search_amazon(search_query)
print("Products found on Amazon:")
for idx, product in enumerate(products, start=1):
    print(f"{idx}. {product}")