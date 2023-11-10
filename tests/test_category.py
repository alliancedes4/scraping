from src.scrapper import scrap_all_categories
from src.scrapper import scrap_all_urls


def test_scrap_all_categories():
    categ_list = scrap_all_categories()
    print(categ_list)