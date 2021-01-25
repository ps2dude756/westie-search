from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    data = [
        {
            'convention': 'Swingtime',
            'year': 2019,
            'format': 'J&J',
            'leads': ', '.join(['Kyle Redd']),
            'follows': ', '.join(['Victoria Henk']),
            'songs': ['Britney Spears - I\'m A Slave 4 U', 'Albin Lee Meldau - The Weight Is Gone (The Purgatory Sessions)'],
            'url': 'https://www.youtube.com/watch?v=JmNOqV9rNIs'
        },
        {
            'convention': 'TAP',
            'year': 2019,
            'format': 'Strictly DJ Battle',
            'leads': ', '.join(['Jakub Jakoubek']),
            'follows': ', '.join(['Victoria Henk']),
            'songs': ['Dr. Dre - The Next Episode (San Holo Remix)'],
            'url': 'https://www.youtube.com/watch?v=8eu82DjxTEE'
        }
    ]
    return render_template('main.html', data=data)
