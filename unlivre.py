import requests
from bs4 import BeautifulSoup
import csv

# Définir l'URL du produit à scraper
url_produit = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

# Créez un fichier CSV unique avec les en-têtes
with open('unlivre_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ["Product URL", "Title", "Price", "Description du produit", "Disponibilité", "UPC", "URL de la page du produit", "Quantité disponible", "Nombre de critiques", "Prix (hors taxe)", "Prix (incl. taxe)", "Note d'évaluation"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    response = requests.get(url_produit)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Code pour extraire les informations du produit
    product_description_div = soup.find("meta", {"name": "description"})
    product_description = product_description_div["content"].strip()
    print("Description du produit:", product_description)

    page_title = soup.find("h1").text.strip()
    print("Titre de la page:", page_title)

    availability = soup.find("p", class_="availability").text.strip()
    print("Disponibilité:", availability)

    upc = soup.find("th", string="UPC").find_next("td").text.strip()
    print("UPC:", upc)

    product_page_url = url_produit
    print("URL de la page du produit:", product_page_url)

    number_available = soup.find("th", string="Availability").find_next("td").text.strip().split("(")[-1].replace(" available)", "").strip()
    print("Quantité disponible:", number_available)

    num_reviews = soup.find("th", string="Number of reviews").find_next("td").text.strip()
    print("Nombre de critiques:", num_reviews)

    price_excl_tax = soup.find("th", string="Price (excl. tax)").find_next("td").text.strip()
    print("Prix (hors taxe):", price_excl_tax)

    price_incl_tax = soup.find("th", string="Price (incl. tax)").find_next("td").text.strip()
    print("Prix (incl. taxe):", price_incl_tax)

    review_rating = soup.find("p", class_="star-rating")["class"][-1]
    print("Note d'évaluation:", review_rating)

    breadcrumb_list = soup.find("ul", class_="breadcrumb")
    category_element = breadcrumb_list.find_all("li")[2].text.strip()

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

    writer.writerow(product_info)  # Écrire les informations dans le fichier CSV
