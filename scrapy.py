from requests import get
from bs4 import BeautifulSoup as bso
import lxml
class Parser:
    def __init__(self, url):
        self.response = get(url)
        self.parsed = None
        self.status = self.response.status_code
        if (self.status == 200):
            self.parsed = self.parse()
    def __str__(self):
        return f"Status code: {self.status}"
    def parse(self):
        return bso(self.response.text, 'lxml')
    def getBlock(self, type, name):
        return self.parsed.find_all(type, class_=name)
    def GetParams(self, blocks, out=[]):
        for block in blocks:
            text = block.find('div', class_='reviewer-name-line"')
            out.append(text.prettify())
        return out

go = Parser("https://www.ceneo.pl/77397396")

print(go)
This = go.getBlock("li","review-box")
print(go.GetParams(This))