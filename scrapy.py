from requests import get
from bs4 import BeautifulSoup as bso
from json import dump


class Ceneo:
    def __init__(self, id):
        self.response = get('https://www.ceneo.pl/' + id)
        self.parsed = None
        self.status = self.response.status_code
        if (self.status == 200):
            self.parsed = self.parse()

    def __str__(self):
        return "Status code: {}".format(self.status)

    def parse(self):
        return bso(self.response.text, "html.parser")

    def opinions(self, dictionary={}):
        opinions = self.parsed.select("li.review-box")
        for opinion in opinions[0:6]:
            author = opinion.find(
                'div', {"class": 'reviewer-name-line'}).string
            #accepted = opinion.find('div', {'class': 'product-review-pz'}).em.string
            #date_out = opinion.findAll('time')[0].string

            try:
                pros = ", ".join(opinion.find(
                    'div', {'class': 'pros-cell'}).ul.get_text().strip().split("\n"))
            except:
                pros = None

            try:
                cons = ", ".join(opinion.find(
                    'div', {'class': 'cons-cell'}).ul.get_text().strip().split('\n'))
            except:
                cons = None

            dictionary[author.replace("\n", "").replace(" ", "")] = {
                'id': opinion["data-entry-id"],
                'recommendation': opinion.find('em', {"class": "product-recommended"}).string,
                'content': opinion.find('p', {'class': 'product-review-body'}).string,
                'score': opinion.find('span', {'class': 'review-score-count'}).string,
                'useful': opinion.find('button', {'class': 'vote-yes'}).span.string,
                'useless': opinion.find('button', {'class': 'vote-no'}).span.string,
                'buy_date': opinion.findAll('time')[1].string,
                'cons': cons,
                'pros': pros}
        return dictionary


product = Ceneo("77397396")

print(product)
if product.status == 200:
    with open('Opinions.json', 'w', encoding='utf-8')as file:
        dump(product.opinions(), file, ensure_ascii=False, indent=4)
