import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":
    url = "https://uk.wikipedia.org/wiki/%D0%A2%D0%B5%D0%B4_%D0%A7%D0%B0%D0%BD"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        #print(soup.prettify())
        print(soup.title.string)
        #divs = soup.find_all("div", class_=)
        base_div = soup.select_one("#mw-contect-text > div")
        print(base_div)
    else:
        print(f"Got{response.status_code}")
