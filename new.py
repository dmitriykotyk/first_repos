import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://steamcommunity.com/"
FILE_NAME = "test.csv"


r = requests.get(URL_TEMPLATE)
print(r.status_code)