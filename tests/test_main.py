from src.scrapper import scrap_all_urls
from src.consts import BASE_URL
from src.scrapper import scrap_info_url


def test_scrap_all_urls():
    result = scrap_all_urls(BASE_URL)  # Remplacez l'URL par celle que vous souhaitez tester
    assert result is not None 
    pass

def test_scrap_info_url():
    result = scrap_info_url("BASE_URL")
    assert result is not None
    pass