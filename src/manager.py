import requests

from src.file_manager import validate_data_dir 
from src.consts import category_names
from bs4 import BeautifulSoup
from src.consts import BASE_URL


def manages_all_categories(base_url:str=BASE_URL): 
    """scrap all categories from the website"""

    # verif si le dossier data existe
    validate_data_dir()
    # scrapper la liste des categories
    

    # sauvegarder la liste des categories dans un fichier 
    


    print("Scraping all categories is done")


def manage_all_urls_categ(url_categorie:str=category_names):

    return manage_all_urls_categ()

    

def scrap_all_books_from_categ():
    
    return scrap_all_books_from_categ()
    
    pass 