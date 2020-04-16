from bs4 import BeautifulSoup
import requests
import urllib.request


def _get_poster_url(imdb_id):
    page = requests.get(imdb_id)
    soup = BeautifulSoup(page.content, 'html.parser')
    poster_div = soup.find_all('div', class_='poster')
    return poster_div.pop(0).find('img').get('src')


def _dl_poster(url):
    with urllib.request.urlopen(url) as u:
        with open('temp.jpg', 'wb') as f:
            f.write(u.read())


def get_poster(imdb_url):
    poster_url = _get_poster_url(imdb_url)
    _dl_poster(poster_url)


if __name__ == '__main__':
    get_poster("https://www.imdb.com/title/tt9148706")

