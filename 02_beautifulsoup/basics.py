from bs4 import BeautifulSoup
from urllib.request import urlopen

"Basic usage of beautiful soup"

""" EXERCISE 1 """
# url = "http://olympus.realpython.org/profiles/dionysus"
# page = urlopen(url)
# html = page.read().decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")
# print(soup) # the html
# print(soup.get_text()) # only the html text, without the tags

# img1, img2 = soup.find_all("img") # returns a list with the whole element (tag and content)
# print(img1.name) # "img"
# print(img1["src"]) # "/static/dionysus.jpg"

"""EXERCISE 2
# Write a program that grabs the full HTML from the 
# page at the URL http://olympus.realpython.org/profiles"""

base_url = "http://olympus.realpython.org"
html_page = urlopen(base_url + "/profiles")
html = html_page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

links_list = soup.find_all("a")

for link in links_list:
  link_url = base_url + link["href"]
  print(link_url)