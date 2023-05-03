from flask import Flask, render_template, redirect, request
from shortener import Shortener
import sys

app = Flask(__name__, template_folder="")
shortener1 = Shortener()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    url = request.form.get('url')
    short_url = shortener1.shorten(url)
    return render_template('result.html', short_url = short_url)

@app.route('/<short_url>')
def redirect_to_url(short_url):
    shortener = Shortener()
    url = shortener.get_url(short_url)
    return redirect(url) if url else "Url not found"

if __name__ == '__main__':
    #DO not remove any Code below
    port = int(sys.argv[1])
    app.run(debug=True, host="0.0.0.0", port=port)
