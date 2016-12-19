## PR0N MINTS


### What is Pr0n Mints exactly?

Pr0n Mints (http://pr0n-mints.herokuapp.com) is just a silly website that scrapes comments
from random YouPorn videos and prints them. Just for your leisure! (**WARNING: Possibly NSWF. Reader discretion advised**)


### But why?

1. Shits
2. Giggles


### And how?

This is built using Python's [Flask](http://flask.pocoo.org/), [JQuery](https://jquery.com/), [Bootstrap](http://getbootstrap.com/)
and all is hosted on [Heroku](https://heroku.com).
The main scraping is done using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

### Roadmap

- (Dec 19, 2016) *Ver 0.0.1*: fetches a random video, scrapes its commits and sorts them by rating, then returns a random one; first release.
- (TBD) *Ver 0.0.5*: add a loading spinner; add transitions between mints.
- (TBD) *Ver 0.1.0*: automatically try another video if no comments are present; possibly investigate YP's apis?
- (TBD) *Ver 1.0.0*: add database capability to save favourites; fetch from db; add new tab to save new fresh mints; improve UI; share button!
