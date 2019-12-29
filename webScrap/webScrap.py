import requests
import urllib.request
import time
from bs4 import BeautifulSoup

class webScrap:

    url = 'http://web.mta.info/developers/turnstile.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.findAll('a')