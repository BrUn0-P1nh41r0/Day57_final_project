from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    post = Post()
    return render_template("index.html", post=post.data)

@app.route('/post/<num>')
def post_info(num):
    post = Post().data
    post_div = []
    for data in post:
        if data["id"] == int(num):
            post_div.append(data)
    return render_template("post.html", post=post_div)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
