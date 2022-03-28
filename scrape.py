from cgitb import html
from bs4 import BeautifulSoup
import requests

starturl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

headers = ["name","distance","mass","radius"]
data = []

page = requests.get(html)
print(page)