# OPENCLASSROOMS - Python Application Developer

## SCRAPING PROJECT

This Python project consists of creating a scraping application to analyze the site http://books.toscrape.com/.

---

### Virtual environment

Here are the commands:
python -m venv scraping
source scraping/bin/activate
pip install -r requirement.txt

---

### Installing the virtual environment

Activate the virtual environment using the appropriate command depending on your operating system:

On Windows: .\scraping\Scripts\activate
On macOS and Linux: source scraping/bin/activate
install the required libraries using the following command: pip install requests bs4 os-csv

---

### Executing the code
activated the virtual environment as explained above.
To run the code, run the Python file using the following command: py scraping.py

---

# Python code for scraping (scraping.py)

```
python
import bone
import requests
import csv
from bs4 import BeautifulSoup

# The Python code goes here...

print("Extraction completed successfully!")

