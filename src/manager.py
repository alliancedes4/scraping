from src.consts import BASE_URL
from src.file_manager import validate_data_dir 


def manage_all_categories(base_url:str=BASE_URL): 
    """scrap all categories from the website"""

    # verif si le dossier data existe
    validate_data_dir()
    # scrapper la liste des categories
    

    # sauvegarder la liste des categories dans un fichier 
    


    print("Scraping all categories is done")