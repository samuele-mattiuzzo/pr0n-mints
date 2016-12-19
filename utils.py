from BeautifulSoup import BeautifulSoup
from random import randrange
import os
import urllib


URL = 'http://www.youporn.com/random/video/'

# {0} is the comment, {1} is the author, {2} is the title
HTML_SNIPPET = """
    <blockquote>
      <p>{0}</p>
      <footer>by {1} in <cite title="{2}">{2}</cite></footer>
    </blockquote>
"""

MAX_COMMENT_LENGTH = 100  # chars


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
        title = soup.find('div', {'class': 'watchVideoTitle'}).find('h1', {'class': 'heading2'}).text.strip()
        for div in comments:
            comment_id = div['data-commentid']

            author = div.find('div', {'class': 'userCommentBox'}).find('span').text.strip()
            comment = div.find('div', {'class': 'commentContent'}).find('p').text.strip()
            rating = div.find('button', {'data-commentid': comment_id, 'class': 'button rateComment like'})
            rating = rating.text.strip().replace('(', '').replace(')', '')

            try:
                if len(str(comment)) <= MAX_COMMENT_LENGTH:
                    result.append((str(comment), str(author), str(title), int(rating)))
            except:
                fetch_mint(tries_left)

        result = sorted(result, key=lambda res: res[3])
        selected = result[randrange(len(result))]
        return HTML_SNIPPET.format(*selected)
