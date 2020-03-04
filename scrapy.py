from requests import get
from bs4 import BeautifulSoup
class Parser:
    def __init__(self, url):
        self.response = get(url)
    def status(self):
        return {
            "status_code": self.response.status_code,
            "timing": self.response.elapsed}
    def parse(self):
        html_soup = BeautifulSoup(self.response.text, 'html.parser')
        job_elems = html_soup.find_all('ol', class_='pproduct-reviews js_reviews-hook')
        return job_elems

go = Parser("https://www.ceneo.pl/77397396")
print(go.status())
print(go.parse())