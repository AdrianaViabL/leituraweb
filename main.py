import json
import re

from bs4 import BeautifulSoup
import requests


def web_reader(link_list):
    request = []
    logo_url = []
    reg = r"(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})"
    for page in link_list:
        try:
            html_page = requests.get(page)
            soup = BeautifulSoup(html_page.content, 'html.parser')
            getStuff = soup.findAll('img', {'src': re.compile('png')})
            phone = re.findall(reg, soup.text)
            for stuff in getStuff:
                if 'logo' in stuff['src']:
                    if 'http' in stuff['src']:
                        logo_url.append(stuff['src'])
                    else:
                        logo_url.append(f"{page}{stuff['src']}")
            result = dict({
                'logo': logo_url,
                'phone': phone,
                'website': page})
            request.append([result])
        except Exception as ex:
            request.append({'erro_message': f'erro no processo {ex}'})
    return json.dumps(request)


if __name__ == '__main__':
    link_list = []
    web_reader(link_list)
