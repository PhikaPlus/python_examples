# By Reza Shah. (Instagram: Phika.ir)
# ===================================
import requests
import bs4

data = requests.get('https://www.goodreads.com/'
                    'search?utf8=%E2%9C%93&q=Sweden&search_type=books')
soup = bs4.BeautifulSoup(data.text, features="html.parser")
a = soup.select('.bookTitle span')

for i in range(len(a)):
    name = a[i].text
    print('Book #{}'.format(i), '\t', name)
