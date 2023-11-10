import os
import pytest
from src.file_manager import save_categ_file, create_each_categ_folder, validate_data_dir

# Test pour save_categ_file
def test_save_categ_file():
    data_to_save = [{"category": "example1", "value": 42}, {"category": "example2", "value": 78}]

    # Appelez la fonction à tester
    save_categ_file(data_to_save)

    # Vérifiez que le fichier a été créé avec succès
    assert os.path.exists('data/categories.csv')

# Test pour create_each_categ_folder
def test_create_each_categ_folder():
    categ_list = ["example1", "example2", "example3"]

    # Appelez la fonction à tester
    create_each_categ_folder(categ_list)

    # Vérifiez que les dossiers ont été créés avec succès
    assert all(os.path.exists(os.path.join('data', category)) for category in categ_list)

# Test pour validate_data_dir
def test_validate_data_dir():
    # Appelez la fonction à tester
    validate_data_dir()

    # Vérifiez que le dossier a été créé avec succès
    assert os.path.exists('data')
