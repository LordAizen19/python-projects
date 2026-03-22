from bs4 import BeautifulSoup
import requests

source = requests.get('https://opencode.ai').text
soup = BeautifulSoup(source, 'lxml')

section = soup.select_one('section[data-component="hero"]')

if section is None:
    print("Section not Found, site may require JavaScript Rendering")
else:
    h1 = section.find('h1')
    if h1:
        print("Heading: ", h1.text.strip())

    p = section.find('p')
    if p:
        print('Description: ', p.get_text(strip=True))

section_what = soup.select_one('section[data-component="what"]')

if section_what is None:
    print("Section not Found, site may require JavaScript Rendering")
else:
    h3 = section_what.find('h3')
    if h3:
        print('Heading: ', h3.text.strip())

    p = section_what.find('p')
    if p:
        print('Description: ', p.get_text(strip=True))

    ul = soup.find('ul')
    items = ul.find_all('li')

    for item in items:
        print(item.text.strip())



