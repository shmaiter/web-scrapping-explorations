from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
# print(soup) # the html
# print(soup.get_text()) # only the html text, without the tags

# img1, img2 = soup.find_all("img") # returns a list with the whole element (tag and content)
# print(img1.name)
# print(img1["src"])

print(soup.tagStack())