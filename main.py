import json
import re

from bs4 import BeautifulSoup
import requests


def web_reader(link_list):
    request = []
    logo_url = []
    reg = r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))'
    for page in link_list:
        html_page = requests.get(page)
        if html_page.status_code != 200:

            break
        soup = BeautifulSoup(html_page.content, 'html.parser')
        getStuff = soup.findAll('img', {'src': re.compile('png')})
        phone = soup.findAll('text', re.compile(reg))
        for stuff in getStuff:
            logo_url.append(f"{page}{stuff['src']}")
        result = dict({
            'logo': logo_url,
            'phone': phone,
            'website': page})
        request.append(result)
        print(getStuff)
    return json.dumps(request)


if __name__ == '__main__':
    link_list = ['https://pt.wikipedia.org/wiki/Portal:Hist%C3%B3ria',
                 'https://stackoverflow.com/questions/3868753/find-usa-phone-numbers-in-python-script/28864077#28864077']
    web_reader(link_list)
