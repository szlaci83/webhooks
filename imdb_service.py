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
    search_url = "https://www.imdb.com/find?q=%s&ref_=nv_sr_sm" % search_term
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



def get_imdb_id(torrent_title):
    movie_title = PTN.parse(torrent_title).get('title', '')
    return _search_for_id(movie_title)


def get_poster_by_name(torrent_title):
    try:
	get_poster("https://www.imdb.com%s" % get_imdb_id(torrent_title))
	return True
    except:
        return None

if __name__ == '__main__':
    title = "Pineapple.Express.UNRATED.PROPER.720p.BluRay.x264-SEPTiC"
    get_poster_by_name(title)
