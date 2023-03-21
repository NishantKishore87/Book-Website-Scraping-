from bs4 import BeautifulSoup
import requests
dict={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
j=1
with open(f'BookswithFiveandFourStarRating.txt','w',encoding='utf-8') as f:
    while(True):
        r=requests.get(f'http://books.toscrape.com/catalogue/page-{j}.html').text
        soup=BeautifulSoup(r,'lxml')
        soup.prettify()
        if(soup.title.text=='404 Not Found'):
                print('End of Result')
                break

        ratings=soup.findAll('article', class_='product_pod')
        names=soup.findAll('h3')
        links = soup.findAll('h3')
        prices = soup.findAll('p', class_='price_color')
        c=1
        for index,rating in enumerate(ratings):
            name=(names[index].a['title'])
            stars=(ratings[index].p['class'][1])
            link = links[index].a['href']
            price = prices[index].text[1:]
            if(dict[stars]>=4):
                    f.write(f'Book Name: {name}\n Book Price: {price}\n Book Link:{link}\n')
                    f.write('\n')
        f.write(f'-------------------------------End of results from PAGE {j}----------------------------------------\n')
        print(f'Page {j} saved\n')
        c=c+1
        j=j+1
f.close()




