from BeautifulSoup import BeautifulSoup
from random import randrange
import os
import urllib
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# some settings vars
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
IS_PRODUCTION = os.environ.get('IS_PRODUCTION', False)
DEBUG = not IS_PRODUCTION

URL = "http://www.youporn.com/random/video/"


# main views
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')


@app.route('/mint-please/')
def mint_please():
    """Api view that fetches a new mint."""
    html_file = urllib.urlopen(URL)
    soup = BeautifulSoup(html_file.read())

    result = []
    for div in soup.findAll("div", {"class": "videoComment"}):
        comment_id = div["data-commentid"]
        comment = div.find("div", {"class": "commentContent"}).find("p").text.strip()
        rating = div.find("button", attrs={"data-commentid": comment_id})
        rating = 0 if rating == '' else int(rating.text.strip())

        if rating >= 0:
            result.append((comment, rating))

    # finds all the comments and picks a random one
    result = sorted(result, key=lambda res: res[1])
    return result[randrange(len(result))]


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=DEBUG)
