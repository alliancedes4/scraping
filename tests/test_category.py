from src.scrapper import scrap_all_categories

def test_scrap_all_categories():
    categories = scrap_all_categories()
    print(categories)