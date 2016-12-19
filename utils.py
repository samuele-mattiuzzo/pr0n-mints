from BeautifulSoup import BeautifulSoup
from random import randrange
import os
import urllib


URL = 'http://www.youporn.com/random/video/'

def fetch_mint(tries=5):
    """ Sends a request to the url. Checks if there are comments. Returns a random one.
    If no comments are present, retries (to a max of 5 times, then bails). """

    tries_left = tries - 1

    if tries_left < 0:
        return 'Whoops! Seems like I couldn\'t find mints for you. Try again maybe?'

    html_file = urllib.urlopen(URL)
    soup = BeautifulSoup(html_file.read())

    comments = soup.findAll('div', {'class': 'videoComment'})

    if not len(comments):
        return fetch_mint(tries_left)
    else:
        result = []
        for div in comments:
            comment_id = div['data-commentid']

            comment = div.find('div', {'class': 'commentContent'}).find('p').text.strip()
            rating = div.find('button', {'data-commentid': comment_id, 'class': 'button rateComment like'})
            rating = rating.text.strip().replace('(', '').replace(')', '')

            result.append((str(comment), int(rating)))

        result = sorted(result, key=lambda res: res[1])
        return result[randrange(len(comments))][0]
