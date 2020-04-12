import requests
from bs4 import BeautifulSoup

response = requests.get("http://unkno.com/")

soup = BeautifulSoup(response.content, "html.parser")

random_fact = soup.find_all(id="content")

print(random_fact[0].getText().strip())