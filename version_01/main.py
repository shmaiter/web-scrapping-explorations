from urllib.request import urlopen
import re
"""First approximation to web scrapping using urllib.request and urlopen
everything is done completely manually, with string methods
"""
# LEVEL 1 = FIND METHOD AND SLICING
# url = "http://olympus.realpython.org/profiles/aphrodite"
# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# print(html)

# title_index = html.find("<title>")
# start_index = title_index + len("<title>")
# end_index = html.find("</title>")
# title_content = html[start_index:end_index]
# print(title_content)

# LEVEL 2 = REGULAR EXPRESSIONS
# url = "http://olympus.realpython.org/profiles/poseidon"
# page = urlopen(url)
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# # print(html)

# pattern = "<title.*?>.*?</title.*?>"
# match_results = re.search(pattern, html, re.IGNORECASE)
# # print(match_results)
# title = match_results.group()
# title = re.sub("<.*?>", "", title) # Remove HTML tags

# print(title)

# LEVEL 3 = CALCULATING INDEXES
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)

for string in ["Name: ", "Favorite Color: "]:
  string_start_index = html.find(string)
  text_start_index = string_start_index + len(string)
  # print(html[text_start_index])
  
  offset_next_tag = html[text_start_index:].find("<")
  text_end_index = text_start_index + offset_next_tag
  
  raw_text = html[text_start_index:text_end_index]
  clean_text = raw_text.strip(" \r\n\t")
  
  print(raw_text)