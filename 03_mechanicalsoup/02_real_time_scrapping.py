import mechanicalsoup
import time

browser = mechanicalsoup.StatefulBrowser()

for _ in range(4):
  page_response = browser.open("http://olympus.realpython.org/dice")
  page_html = page_response.soup
  tag = page_html.select("#result")[0]
  result = tag.text

  print(f"The result of your dice roll is: {result}" )
  if _ < 3:
    time.sleep(5)
  