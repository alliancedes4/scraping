import os

import requests
from bs4 import BeautifulSoup

from src.consts import BASE_URL
from src.consts import CATEGORY_URL
from src.extractor import extract_categories

def scrap_all_categories(base_url: str = BASE_URL) -> list:
    """Scarp all categories frome tje website"""

    #request la page
    response = requests.get(BASE_URL)

    # soup de la page de notre page 
    soup = BeautifulSoup(response.text, "html.parser")

    # extract categories form main page
    categ_list = extract_categories(soup)

    # Extraire les noms des catégories à partir des URL
    category_names = [CATEGORY_URL.split("/")[-2].split("_")[0] for url in categ_list]
    print("Scraping all categories is done. Category names:", category_names)

    return categ_list





# def scrap_all_urls(base_url):
    #"""Scrap all URLs from the website and print them."""
    # Envoyer une requête HTTP pour obtenir le contenu de la page principale
    #response = requests.get(base_url)

    # Analyser le contenu HTML de la page avec BeautifulSoup
    #soup = BeautifulSoup(response.text, 'html.parser')

    # Extraire tous les liens de catégorie
    #links = soup.find_all('h3')

    # Parcourir les liens et imprimer les URLs
    #for link in links:
            #href = link.a['href']
            #print(href)

    #else:
        #print("La requête a échoué avec le code de statut", response.status_code)


