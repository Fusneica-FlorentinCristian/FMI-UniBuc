import json
import pprint
import random
import threading
from urllib.request import Request, urlopen
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from requests.exceptions import ProxyError
from tqdm import tqdm as tqdm_notebook
import requests
import re
import bs4
import re
from itertools import cycle

from urllib3.exceptions import MaxRetryError


def check_proxy_usage(proxy_type, proxy):
    try:
        final_proxy = f'{proxy_type}://{proxy}'
        print(proxy_type, proxy)
        verify = requests.get('https://httpbin.org/ip', proxies={proxy_type: final_proxy}, verify=False)
        verify = verify.json()['origin'] if 200 <= verify.status_code < 299 else None

        # assert final_proxy == verify, f'{proxy} is not the same as {verify}'

        return verify == final_proxy
    except Exception as e:
        print(f"Proxy not verified {e.args}")
        return True


def get_custom_proxy_list():

    proxy_request = requests.get('https://free-proxy-list.net/')

    if not (200 <= proxy_request.status_code < 299):
        raise Exception('Doesn\'t connect to proxy')

    proxy_soup = BeautifulSoup(proxy_request.text, 'html.parser')
    table = proxy_soup.find('table').tbody.find_all('tr')
    table_extracted_data = [elem.find_all('td')[0:7] for elem in table]
    table_extracted_data = [(f'http{"" if elem[6].text == "no" else "s"}', f'{elem[0].text}:{elem[1].text}')
                            for elem in table_extracted_data if elem[4].text == "elite proxy"]

    return cycle(table_extracted_data)


class MusixmatchScraper:
    """This class allows you to scrape the lyrics for an artist who has a presence on Musixmatch

    An instance of the class needs to be instantiated with an artist URL e.g.

    https://www.musixmatch.com/artist/Bob-Dylan

    The default number of songs to scrape is 50

    """

    def __init__(self, artist_url, genre_label=None, custom_proxy_list=None):

        self.artist_url = artist_url  # artists URL as attribute

        self.artist = artist_url.split('artist/')[-1]  # artist string as attribute

        self.genre_label = genre_label  # genre as attribute

        self.song_l = []  # empty list to populate lyrics

        self.proxies = get_custom_proxy_list() if not custom_proxy_list else custom_proxy_list

    def _get_html(self, url):

        """Uses Beatiful Soup to extract html from a url. Returns a soup object """

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        }

        proxy_type, proxy = next(self.proxies)
        while True:
            try:
                print('Requesting resources...')
                req = requests.get(url, headers=headers, proxies={proxy_type: f'{proxy_type}://{proxy}'}, verify=False, timeout=10)
                # print(req.text if req.status_code == 200 else "Not much to show for this request")
                # print( req.text.find("https://www.google.com/recaptcha/api.js"))
                assert req.text.find("https://www.google.com/recaptcha/api.js") == -1, "Yeah, you have run into a captcha"

                return BeautifulSoup(req.text, 'html.parser')
            except ProxyError as e:
                print(f"Try {proxy} with https")
                proxy_type += "s"
                continue
            except (OSError, MaxRetryError) as e:
                print(f'Verify proxy on init after simple errors')
                while check_proxy_usage(proxy_type, proxy):
                    print(f'Ordinary error appeared: {e.args}\nNext proxy: {proxy}\n')
                    proxy_type, proxy = next(self.proxies)
                else:
                    proxy_type, proxy = next(self.proxies)

                continue
            except Exception as e:
                print(*e.args)
                while check_proxy_usage(proxy_type, proxy):
                    print(f'Ordinary error appeared: {e.args}\nNext proxy: {proxy}\n')
                    proxy_type, proxy = next(self.proxies)
                else:
                    proxy_type, proxy = next(self.proxies)

                continue


        return None

    def _multithreadCompile(self, thread_count, iteration_list, func):

        """a function that compiles an iteration list to prepare
        multi threadding"""

        jobs = []

        # distribute iteration list to batches and append to jobs list
        batches = [i.tolist() for i in np.array_split(iteration_list, thread_count)]

        for i in range(len(batches)):
            jobs.append(threading.Thread(target=func, args=[batches[i]]))

        return jobs

    def _multithreadExecute(self, jobs):

        """executes the multi-threadding loop"""

        # Start the threads
        for j in jobs:
            j.start()

        # Ensure all of the threads have finished
        for j in jobs:
            j.join()
        return

    def _getpageUrls(self, url):

        """Gets all the links from an artist page"""

        html = self._get_html(url)  # gets html for current page
        # print("Returned HTML")
        # pprint.pprint(html)

        if html is None:
            return []

        songs = html.find_all('h2', {'class': 'media-card-title'})  # element for song

        # loop through and extract urls for all songs in soup object
        song_urls = [f'https://www.musixmatch.com{i.find("a")["href"]}' for i in songs]

        # return list of song urls
        return [i for i in song_urls if 'album' not in i]

    def _getLyrics(self, song_url):

        """Extracts lyrics from a song url. Duplicated lines are removed e.g. chorus lines
        Only unique lyrics are returned"""

        html = self._get_html(song_url)  # get html for current page

        # find all elements containing lyrics
        element = html.find_all('span', {'class': 'lyrics__content__ok'})

        # numbe of elements to loop through
        element_loop = len(element)

        song_lyrics = []  # empty list for song lyrics

        # extract song lyrics
        song_lyrics_raw = [element[i].text.split('\n') for i in range(element_loop)]

        # flatten list of lists
        song_lyrics_raw = [i for sublist in song_lyrics_raw for i in sublist]

        # retain only unique lines in lyrics
        song_lyrics.extend(list(dict.fromkeys(song_lyrics_raw)))

        # join list and remove empty elements
        song_lyrics = ' '.join([i for i in song_lyrics if len(i) > 0])

        return song_lyrics  # return song lyrics

    def _getAllpageUrls(self, target=50):

        """Generates page urls for artist. There are 15 songs on each page"""

        loops = int(target / 15)  # specifcy how many loops needed

        # generate urls
        artist_urls = [self.artist_url + '/' + str(i + 1) for i in range(loops)]

        all_song_urls = []  # empty list for all song urls

        for i in artist_urls:  # loop through and get all song urls for all pages
            url_object = self._getpageUrls(i)
            # pprint.pprint(url_object)
            all_song_urls.extend(url_object)

        return all_song_urls

    def _extractData(self, all_song_urls):

        """Extracts data from all song urls"""

        for i in tqdm_notebook(range(len(all_song_urls))):  # loop through all song urls

            # get lyrics
            song_lyrics = self._getLyrics(all_song_urls[i])

            # get song title
            song_title = all_song_urls[i].split('/')[-1]

            # create DataFrame
            song_df = pd.DataFrame([(self.artist, song_title, song_lyrics)], columns=['artist', 'song', 'lyrics'])

            # append DataFrame to master list
            self.song_l.append(song_df)

    def Run(self, target=50):

        """Executes all methods above"""

        self.all_song_urls = self._getAllpageUrls(target)  # get page URL's to get target number of songs

        # multi-threaded scraping of all song urls
        # print("yey 1")
        # self._multithreadExecute(self._multithreadCompile(5, self.all_song_urls, self._extractData))
        # print("yey")
        self._extractData(self.all_song_urls)
        df_final = pd.concat([i for i in self.song_l])  # concatenate all song Df's

        df_final.reset_index(drop=True, inplace=True)  # reset index

        self.df = df_final.loc[df_final.lyrics.str.len() > 0]  # drop any songs with no lyrics or failed scrapes

        # self.df['genre'] = self.genre_label  # add genre column

        return self.df


def get_artists_page():
    return requests.get(f"https://www.billboard.com/charts/artist-100/")


def parse_html(html):
    return bs4.BeautifulSoup(html, "html.parser")


def get_top_artists():
    html = get_artists_page().content
    soup = parse_html(html)

    entries_texts = []
    #     entries = soup.find_all("h3", {"id": "title-of-a-story", "class":"c-title"})
    return [re.sub(r"[\t\n]+", "", entry.find("h3").text).replace(" ", "-") for entry in
            soup.find_all("div", class_="o-chart-results-list-row-container")]


custom_proxy = get_custom_proxy_list()
artists = get_top_artists()
# print(artists)
BASE_ARTIST_LINK = "https://www.musixmatch.com/artist/"
artists_info = [MusixmatchScraper(f"{BASE_ARTIST_LINK}{artist.lower()}", custom_proxy_list=custom_proxy) for artist in artists]
bob = MusixmatchScraper("https://www.musixmatch.com/artist/Bob-Dylan")
# bob.Run(50)
# ceva = artists_info[0].Run(50)
# print(type(ceva))
# ceva = artists_info[0].df
# artists_info[0].df.pop("artist")
# artists_info[0].df.to_pickle("a_file.pkl")
# print(bob.df)
# print(ceva)
# with open('lil_durk.json', 'w') as fp:
#     json.dump(ceva, fp)
# ceva.to_pickle(f"{artists[0]}.pkl")
for i in range(len(artists)):
    artist_musix = artists_info[i].Run()
    artists_info[i].df.pop("artist")
    with open(f'{artists[i]}.json', 'w') as fp:
        json.dump(artist_musix.to_json(), fp)
