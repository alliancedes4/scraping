
from src.scrapper import scrap_all_categories
from src.consts import BASE_URL
#from src.scrapper import scrap_all_urls


def main():
    """main function of the program"""

    # 1 scrap toute les catégorie 
    scrap_all_categories()

    # 2 pour chaque catégorie 
    
    # je scrap les urls et je save
    #scrap_all_urls()
    # 3 pour chaque url je scrap les infos et je save dans un csv

if __name__ ==  "__main__":
    main()