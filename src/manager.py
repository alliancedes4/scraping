import requests

from bs4 import BeautifulSoup

from src.consts import BASE_URL
from src.file_manager import validate_data_dir 
from src.consts import category_names
from src.scrapper import scrap_all_categories
from src.file_manager import save_categ_file, create_each_categ_folder


def manages_all_categories(base_url: str = BASE_URL): 
    """scrap all categories from the website"""

    # verif si le dossier data existe
    validate_data_dir()

    # scrapper la liste des categories
    categ_list = scrap_all_categories(base_url)

    # sauvegarder la liste des categories dans un fichier 
    save_categ_file(categ_list)

    #fot each categ, create a folder in data to store images (for future use)
    create_each_categ_folder(categ_list)

    print("Scraping all categories is done")


def manage_all_urls_categ(url_categorie: str = category_names):
    """manage all urls fdrom a category"""
    
     # verif si le dossier data existe
    validate_data_dir()   

    return manage_all_urls_categ()

    

def scrap_all_books_from_categ():
    
    return scrap_all_books_from_categ()
    
    pass 