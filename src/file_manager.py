import os

def validate_data_dir(path:str = ".data/"):
    """validate that the data directory exists, if not create it."""

    if not os.path.exists(path):
        print("create data directory")
        os.makedirs(path)


def validate_urls_file(fn:str = ".data/urls.txt"):
    """validate that the urls file exists, if not create it."""
    if not os.path.exists(fn):
        raise FileNotFoundError("file {fn} not found")
    

def save_urls(url_list: list, fn: str = "./data/urls.txt"):
    """save urls to file."""

    with open(fn, "w") as f:
        for url in url_list:
            f.write(f"{url}\n")

def load_urls(fn: str = "./data/urls.txt"):
    """lead urls from file."""

    with open(fn, "r") as f:
        url_list = f.readlines()
    return url_list



# créer des urls

# écrire dans le fichier url

# lire le fichier url


