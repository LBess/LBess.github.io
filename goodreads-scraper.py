from re import I
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.goodreads.com/review/list/94131787-liam-b?shelf=currently-reading")
soupGr = BeautifulSoup(r.content, "html.parser")
sGr = soupGr.find("table", "table stacked")

elements = []
elements.append(sGr.find("th", "header field isbn"))
elements.append(sGr.find("th", "header field isbn13"))
elements.append(sGr.find("th", "header field asin"))
elements.append(sGr.find("th", "header field num_pages"))
elements.append(sGr.find("th", "header field avg_rating"))
elements.append(sGr.find("th", "header field num_ratings"))
elements.append(sGr.find("th", "header field date_pub"))
elements.append(sGr.find("th", "header field date_pub_edition"))
elements.append(sGr.find("th", "header field rating"))
elements.append(sGr.find("th", "header field shelves"))
elements.append(sGr.find("th", "header field review"))
elements.append(sGr.find("th", "header field notes"))
elements.append(sGr.find("th", "header field recommender"))
elements.append(sGr.find("th", "header field comments"))
elements.append(sGr.find("th", "header field votes"))
elements.append(sGr.find("th", "header field read_count"))
elements.append(sGr.find("th", "header field date_read"))
elements.append(sGr.find("th", "header field date_added"))
elements.append(sGr.find("th", "header field date_purchased"))
elements.append(sGr.find("th", "header field owned"))
elements.append(sGr.find("th", "header field purchase_location"))
elements.append(sGr.find("th", "header field condition"))
elements.append(sGr.find("th", "header field format"))
elements.append(sGr.find("th", "header field actions"))

elements += sGr.find_all("td", "field isbn")
elements += sGr.find_all("td", "field isbn13")
elements += sGr.find_all("td", "field asin")
elements += sGr.find_all("td", "field num_pages")
elements += sGr.find_all("td", "field avg_rating")
elements += sGr.find_all("td", "field num_ratings")
elements += sGr.find_all("td", "field date_pub")
elements += sGr.find_all("td", "field date_pub_edition")
elements += sGr.find_all("td", "field rating")
elements += sGr.find_all("td", "field shelves")
elements += sGr.find_all("td", "field review")
elements += sGr.find_all("td", "field notes")
elements += sGr.find_all("td", "field recommender")
elements += sGr.find_all("td", "field comments")
elements += sGr.find_all("td", "field votes")
elements += sGr.find_all("td", "field read_count")
elements += sGr.find_all("td", "field date_read")
elements += sGr.find_all("td", "field date_added")
elements += sGr.find_all("td", "field date_purchased")
elements += sGr.find_all("td", "field owned")
elements += sGr.find_all("td", "field purchase_location")
elements += sGr.find_all("td", "field condition")
elements += sGr.find_all("td", "field format")
elements += sGr.find_all("td", "field actions")

for i in range(len(elements)):
    elements[i].decompose()

with open("layouts/index.html") as file:
    layoutData = file.read()

soup = BeautifulSoup(layoutData, "html.parser")
s = soup.find("div", "recently-read-books")
s.clear()
s.append(sGr)

with open("layouts/index.html", "w") as file:
    file.write(str(soup))