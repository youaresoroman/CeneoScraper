# CeneoScraper11S
# Etap 1 - pobranie pojedynczeej opinii 
- opinia: li.review-box
- identyfikator: li.review-box["data-entry-id"]
- autor: div.reviewer-name-line
- rekomendacja: div.product-review-summary > em
- liczba gwiazdek: span.review-score-count
- czy potwierdzona zakupem: div.product-review-pz
- data wystawienia: span.rewiev-time > time["datetime"] - pierwsze wystąpięnie
- data zakupu: span.rewiev-time > time["datetime"] - drugie wystąpięnie
- przydatna: button.votes - yes['data-total-vote']
- nieprzydatna: button.votes - no['data-total-vote']
- treść: p.product-rewiev-body
- wady: div.cons-cell >  ul
- zalety: div.pros-cell > ul