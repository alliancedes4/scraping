from bs4 import BeautifulSoup

def extract_categories(soup : BeautifulSoup) -> list:
    """Extract categories from  the main page"""

    #find all categories
    categories = soup.find("ul", {"class": "nav nav-list"}).find_all("li")

    #extract categories
    categ_list = []
    for categ in categories:
            categ_list.append(
            {
                "name": categ.find("a").text.strip(),
                "url": categ.find("a").get("href").strip(),
            }
        )
    return categ_list

    