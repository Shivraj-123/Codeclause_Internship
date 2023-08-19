from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

url_database = {}


def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        full_url = request.form['full_url']
        short_code = generate_short_code()
        url_database[short_code] = full_url
        short_url = f"http://localhost:5000/{short_code}"
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', short_url=None)


@app.route('/<short_code>')
def redirect_to_full_url(short_code):
    if short_code in url_database:
        full_url = url_database[short_code]
        return redirect(full_url)
    return "Short URL not found."


if __name__ == '__main__':
    app.run(debug=True)
