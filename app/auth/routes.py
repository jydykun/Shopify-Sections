from flask import render_template, redirect, url_for
from app.auth import bp
from app.auth.forms import PostForm


@bp.route("/post", methods=["POST", "GET"])
def post():
    form = PostForm()
    if form.validate_on_submit():
        fo
        return redirect(url_for("main.index", form=form))
    return render_template("post.html", form=form)

