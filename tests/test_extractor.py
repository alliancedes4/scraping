import requests 
from bs4 import BeautifulSoup
from src.extractor import extract_categories 

from src.consts import BASE_URL

def test_extract_categories() :
    """euh"""

    # requests la page
    reponse = requests.get(BASE_URL)

    # soup de notre page
    soup = BeautifulSoup(reponse.text, "html.parser")

    out = extract_categories(soup)
    print(out)
    