import os
import csv

def validate_data_dir(path:str = "./data/"):
    """validate that the data directory exists, if not create it."""
    if not os.path.exists(path):
        print(f"Creating data directory at '{path}'")
        os.makedirs(path)


def validate_urls_file(fn:str = "/data/urls.txt"):
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


def save_categ_file(data, filename='categories.csv'):
    """Sauvegarde les données de catégorie dans un fichier CSV."""
    try:
        # Assurez-vous que le dossier 'data' existe
        validate_data_dir()

        # Utilisez le chemin spécifié lors de l'appel
        file_path = os.path.join('./data', filename)

        # Le reste de votre fonction reste inchangé
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            if data and isinstance(data[0], dict):
                csv_writer.writerow(data[0].keys())
            for row in data:
                csv_writer.writerow(row.values() if isinstance(row, dict) else row)

        print(f"Les données ont été enregistrées avec succès dans {file_path}")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement des données : {e}")

def create_each_categ_folder(categ_list):
    """Crée un dossier pour chaque catégorie dans le dossier 'data'."""
    try:
        # Assurez-vous que le dossier 'data' existe
        validate_data_dir()

        # Créez un dossier pour chaque catégorie
        for category in categ_list:
            category_path = os.path.join('./data', category)
            os.makedirs(category_path, exist_ok=True)
            print(f"Dossier '{category}' créé avec succès.")
    except Exception as e:
        print(f"Erreur lors de la création des dossiers de catégorie : {e}")



# créer des urls


# écrire dans le fichier url

# lire le fichier url


