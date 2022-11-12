from bs4 import BeautifulSoup
import requests


def web_reader(link_list):
    request = {}
    for page in link_list:
        html_page = requests.get(page)
        if html_page.status_code != 200:
            break
        soup = BeautifulSoup(html_page.content, 'html.parser')

        warning = soup.findAll('img')
        book_container = warning.nextSibling.nextSibling
        print(book_container)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    link_list = ['http://books.toscrape.com/']
    web_reader(link_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
