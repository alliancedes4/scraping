from src.scrapper import manage_all_categories 
from src.scrapper import scrap__all_categories
def main():
    """main function of the program"""

    # 1 scrap toute les catégorie 
    manage_all_categories()
    # 2 pour chaque catégorie 
    scrap__all_categories()
    # je scrap les urls et je save

    # 3 pour chaque url je scrap les infos et je save dans un csv

if __name__ ==  "__main__":
    main()