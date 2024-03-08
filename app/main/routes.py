from flask import render_template
from app.main import bp

posts = [
    {
        "title": "Blog 1",
        "author": "John Doe1",
        "post": "Blog content."
    },
    {
        "title": "Blog 2",
        "author": "John Doe2",
        "post": "Blog content."
    },
    {
        "title": "Blog 3",
        "author": "John Doe3",
        "post": "Blog content."
    }
]



@bp.route("/")
def index():
    return render_template("index.html", posts=posts)