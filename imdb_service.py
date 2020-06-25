from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.parse
import PTN

def _get_poster_url(imdb_id):
    page = requests.get(imdb_id)
    soup = BeautifulSoup(page.content, 'html.parser')
    poster_div = soup.find_all('div', class_='poster')
    return poster_div.pop(0).find('img').get('src')


def _search_for_id(search_term):
    search_term = str(search_term).replace(" ", "+")
    search_url = f"https://www.imdb.com/find?q={search_term}&ref_=nv_sr_sm"
    page = requests.get(search_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    imdb_id = soup.find('td', class_='primary_photo').find('a').get('href')
    return imdb_id


def _dl_poster(url):
    with urllib.request.urlopen(url) as u:
        with open('temp.jpg', 'wb') as f:
            f.write(u.read())


def get_poster(imdb_url):
    poster_url = _get_poster_url(imdb_url)
    _dl_poster(poster_url)


def get_poster_by_name(torrent_title):
    movie_title = PTN.parse(torrent_title).get('title', '')
    imdb_id = _search_for_id(movie_title)
    get_poster(f"https://www.imdb.com{imdb_id}")


if __name__ == '__main__':
    title = "Pineapple.Express.UNRATED.PROPER.720p.BluRay.x264-SEPTiC"
    get_poster_by_name(title)
