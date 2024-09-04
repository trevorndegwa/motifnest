from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Trevor Ndegwa',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'September 4th, 2024'
    },
    {
        'author': 'Corey Schafer',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20th, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
