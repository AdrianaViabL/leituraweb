import json
import os
import re

from bs4 import BeautifulSoup
import requests


def web_reader(link_list):
    request = []
    reg = r"(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})"
    for page in link_list:
        logo_url = []
        try:
            html_page = requests.get(page)
            soup = BeautifulSoup(html_page.content, 'html.parser')
            get_stuff = soup.findAll('img', {'src': re.compile('logo')})
            phone = re.findall(reg, soup.text)
            for stuff in get_stuff:
                if 'logo' in stuff['src']:
                    if 'http' in stuff['src']:
                        logo_url.append(stuff['src'])
                    else:
                        logo_url.append(f"{page}{stuff['src']}")
            result = dict({
                'logo': logo_url,
                'phone': phone,
                'website': page})
            request.append(result)
        except Exception as ex:
            request.append({'erro_message': f'erro no processo {ex}'})
    return json.dumps(request)


if __name__ == '__main__':
    file_name = os.listdir('file/')
    if file_name:
        if '.txt' in file_name[0].lower():
            file_info = open(f"file/{file_name[0]}", "r")
            link_list = [line.rstrip('\n') for line in file_info]
            result = web_reader(link_list)
            file_info.close()
            print(result)
        else:
            print('arquivo com formato invalido')
