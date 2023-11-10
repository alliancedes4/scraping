
from src.scrapper import scrap_all_urls  
from src.consts import BASE_URL

def test_scrap_all_urls():
    
    # Appel de la fonction pour obtenir la liste des liens
    link = scrap_all_urls(BASE_URL)

    # Vérifier que le résultat est une liste
    assert isinstance(link, list)

    # Vérifier que la liste n'est pas vide (vous pouvez ajuster cela en fonction de vos attentes)
    assert len(link) > 0

    # Afficher les liens (facultatif, à des fins de débogage)
    print(link)


