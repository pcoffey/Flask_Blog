from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Jack Bauer',
        'title': 'Blog Post 1',
        'content': 'POSTY content 1',
        'date_posted': 'June 20, 2018'
    },
    {
        'author': 'Shelly Bauer',
        'title': 'Blog Post 20',
        'content': 'POSTY Mc Post content 5',
        'date_posted': 'May 20, 2018'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run()
