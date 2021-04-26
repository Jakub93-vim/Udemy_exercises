import lxml
import requests
import bs4

result = requests.get("http://quotes.toscrape.com/")

soup = bs4.BeautifulSoup(result.text,"lxml")


#print(soup.select('.author'))

for item in soup.select('.author'):
    print(item.text)

print('\n')

for item in soup.select('.text'):
    print(item.text)

for item in soup.select('.tag-item'):
    print(item.text)

#try:
list_of_authors = []
set_of_authors = set ()

for n in range(1,15):
    authors = requests.get(f"http://quotes.toscrape.com/page/{n}/")
    author = bs4.BeautifulSoup(authors.text,"lxml")

    for item in author.select('.author'):
        if item.text not in list_of_authors:
            list_of_authors.append(item.text)
            set_of_authors.add(item.text)
        else:
            pass

print(list_of_authors)
print(set_of_authors)

#except:

  #  print('Too many pages')
