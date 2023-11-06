import os

import requests
from bs4 import BeautifulSoup

from src.consts import BASE_URL
from src.consts import category_names
from src.extractor import extract_categories


def scrap_all_categories(base_url: str = BASE_URL) -> list:
    """Scarp all categories frome tje website"""
         
    #request la page
    response = requests.get(BASE_URL)

    # soup de la page de notre page 
    soup = BeautifulSoup(response.text, "html.parser")

    # extract categories form main page
    categ_list = extract_categories(soup)
    print(categ_list[0])

    # Extraire les noms des catégories à partir des URL
    category_names = [url.split("/")[-2].split()[] for url in categ_list]
    #category_names = [url.split("/")[-2].split("_")[0] for url in categ_list]
    print("Scraping all categories is done. Category names:", category_names)

    return categ_list
    

def scrap_all_urls(base_url):
    """Scrape all URLs from the website and print them."""
    # Send an HTTP request to fetch the content of the main page
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all category links
        links = soup.find_all('h3')

        # Iterate through the links and print the URLs
        for link in links:
            href = link.a['href']
            print(href)
    else:
        print("The request failed with status code", response.status_code)




