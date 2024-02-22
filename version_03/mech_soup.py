import mechanicalsoup

"""Submit username and password inside a login form"""

# 1
browser = mechanicalsoup.StatefulBrowser()
base_url = "http://olympus.realpython.org"
url = base_url + "/login"
login_page = browser.open(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

# 4
# print(profiles_page.url)
# print(profiles_page.soup)


"""programmatically obtain the URL for each link on the /profiles page"""
profiles_html = profiles_page.soup
print(profiles_html.title)
links_list = profiles_html.select("a")

for link in links_list:
  address = base_url + link["href"]
  text = link.text
  print(f"{text}: {address}")
  # print(browser.get(address).soup)
  # print(browser.get(address).soup.get_text())