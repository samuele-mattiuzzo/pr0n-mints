import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# some settings vars
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
IS_PRODUCTION = os.environ.get('IS_PRODUCTION', False)
DEBUG = not IS_PRODUCTION


# main views
@app.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')


@app.route('/mint-please/')
def mint_please():
    """Api view that fetches a new mint."""
    return 'hi'


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=DEBUG)
