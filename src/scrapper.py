import os
import csv

import requests
from bs4 import BeautifulSoup

from src.consts import BASE_URL
from src.consts import category_names
from src.extractor import extract_categories
from src.extractor import extract_info_url


def scrap_all_categories(base_url: str = BASE_URL) -> list:
    """Scarp all categories frome tje website"""
         
    #request la page
    response = requests.get(BASE_URL)

    # soup de la page de notre page 
    soup = BeautifulSoup(response.text, "html.parser")

    # extract categories form main page
    categ_list = extract_categories(soup)

    #extract name of categ from categ_list
    categ_list = [i["name"] for i in categ_list]

    #logging
    #print(categ_list)

    return categ_list
    

def scrap_all_urls(base_url):
    """Scrape all URLs from the website and return them in a list."""
    
    # Send an HTTP request to fetch the content of the main page
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all category links
        links = soup.find_all('h3')

        # Initialize a list to store the URLs
        url_list = []

        # Iterate through the links and collect the actual URLs
        for link in links:
            # Check if the link has an 'a' tag and an 'href' attribute
            if link.a and 'href' in link.a.attrs:
                href = link.a['href']
                url_list.append(href)
        
        return url_list
    else:
        print("The request failed with status code", response.status_code)
        return []  # Return an empty list in case of failure


def scrap_info_url(url_produit: str):
    """Scrape information from a specific product URL."""
    try:
        # Send an HTTP request to fetch the content of the product page
        response = requests.get(url_produit)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Code pour extraire les informations du produit
            product_description_div = soup.find("meta", {"name": "description"})
            product_description = product_description_div["content"].strip()

            page_title = soup.find("h1").text.strip()
            availability = soup.find("p", class_="availability").text.strip()
            upc = soup.find("th", string="UPC").find_next("td").text.strip()
            product_page_url = url_produit
            number_available = soup.find("th", string="Availability").find_next("td").text.strip().split("(")[-1].replace(" available)", "").strip()
            num_reviews = soup.find("th", string="Number of reviews").find_next("td").text.strip()
            price_excl_tax = soup.find("th", string="Price (excl. tax)").find_next("td").text.strip()
            price_incl_tax = soup.find("th", string="Price (incl. tax)").find_next("td").text.strip()
            review_rating = soup.find("p", class_="star-rating")["class"][-1]

            breadcrumb_list = soup.find("ul", class_="breadcrumb")
            category_element = breadcrumb_list.find_all("li")[2].text.strip()

            # Construire un dictionnaire avec les informations du produit
            product_info = {
                "Product URL": url_produit,
                "Description du produit": product_description,
                "Title": page_title,
                "Disponibilité": availability,
                "UPC": upc,
                "URL de la page du produit": product_page_url,
                "Quantité disponible": number_available,
                "Nombre de critiques": num_reviews,
                "Prix (hors taxe)": price_excl_tax,
                "Prix (incl. taxe)": price_incl_tax,
                "Note d'évaluation": review_rating
            }

            return product_info

        else:
            print(f"The request to {url_produit} failed with status code {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred while scraping {url_produit}: {e}")
        return None


# Créez un fichier CSV unique avec les en-têtes
csv_filename = 'unlivre_data.csv'

with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["Product URL", "Title", "Description du produit", "Disponibilité", "UPC", "URL de la page du produit", "Quantité disponible", "Nombre de critiques", "Prix (hors taxe)", "Prix (incl. taxe)", "Note d'évaluation"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Remplacez url_produit par l'URL du produit que vous souhaitez scraper
    url_produit = 'BASE_URL'
    product_info = scrap_info_url(url_produit)

    if product_info:
        writer.writerow(product_info)






