from flask import render_template, redirect, url_for, session, flash
from app.auth import bp
from app.auth.forms import PostForm, LoginForm
from app.main.routes import posts



@bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        session['username'] = username
        return redirect(url_for('auth.post'))
    return render_template('login.html', form=form)

@bp.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('main.index'))

@bp.route("/post", methods=["POST", "GET"])
def post():
    form = PostForm()
    if 'username' in session:
        if form.validate_on_submit():
            post = {
                'title': form.post_title.data.capitalize(),
                'author': session['username'].capitalize(),
                'post': form.post_content.data
            }
            session['post'] = post
            flash("Posted Successfully")
            return redirect(url_for("main.index"))
    return render_template("post.html", form=form)


@bp.route('/edit_post/', methods=['GET', 'POST'])
def edit_post():
    form = PostForm()
    if 'username' in session:
        if form.validate_on_submit():
            posts = [{
                'title': form.post_title.data,
                'post': form.post_content.data,
            }]
            flash("Saved")
            return redirect(url_for("main.index", posts=posts))
    else:
        return "You need to login."
    return render_template("edit_post.html", form=form)

