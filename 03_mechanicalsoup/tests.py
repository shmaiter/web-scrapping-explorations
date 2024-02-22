import mechanicalsoup

url = "http://httpbin.org"
browser = mechanicalsoup.StatefulBrowser()
page_response = browser.open(url)   # <Response [200]>
page_html = page_response.soup

# print(type(page_response))        # <class 'requests.models.Response'>
# print(type(page_response.soup))   # <class 'bs4.BeautifulSoup'>
# print(type(browser.page))         # <class 'bs4.BeautifulSoup'>