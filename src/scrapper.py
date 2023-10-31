import os

import requests
from bs4 import BeautifulSoup

from src.consts import BASE_URL
from src.file_manager import validate_data_dir  
from src.extractor import extract_categories

def scrap_all_categorie(base_url=BASE_URL):
    """Scarp all categories frome tje website"""

    #request la page
    response = requests.get(BASE_URL)

    # soup de la page de notre page 
    soup = BeautifulSoup(response.text, "html.parser")

    # extract categories form main page
    categ_list = extract_categories(soup)

    return categ_list