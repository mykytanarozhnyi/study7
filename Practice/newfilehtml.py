import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    url = "https://docs.python.org/3/library/index.html"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        toctree_div = soup.find("li", class_="l1")
        toctree_div[1:10]
        for child in ul_element:
            link = child.select_one("a")

        #print(soup.title.string)
        #divs = soup.find_all("div", class_=)
        #div_introduction
        #base_div = soup.select("#toctree-wrapper compound > ul > li > a href")
        #print(base_div)
    else:
        print(f"Got{response.status_code}")