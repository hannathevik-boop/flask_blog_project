import os
from flask import Flask, render_template, request, redirect, url_for, abort, flash
from werkzeug.utils import secure_filename
import db

app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    posts = db.get_posts()
    return render_template("home.html", posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = db.get_post(post_id)

    if post is None:
        abort(404)

    comments = db.get_comments(post_id)

    return render_template(
        "post.html",
        post=post,
        comments=comments
    )


@app.route("/create", methods=["GET", "POST"])
def create():

    if request.method == "POST":

        title = request.form["title"]
        body = request.form["body"]
        tags = request.form["tags"]

        image_file = request.files.get("image")
        image_filename = None

        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image_file.save(image_path)
            image_filename = filename

        if not title or not body:
            abort(400)

        db.create_post(title, body, tags, image_filename)

        flash("Blog post created successfully!")

        return redirect(url_for("home"))

    return render_template("create_post.html")


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):

    post = db.get_post(post_id)

    if post is None:
        abort(404)

    if request.method == "POST":

        title = request.form["title"]
        body = request.form["body"]
        tags = request.form["tags"]

        db.update_post(post_id, title, body, tags)

        flash("Post updated successfully!")

        return redirect(url_for("post", post_id=post_id))

    return render_template("edit_post.html", post=post)


@app.route("/comment/<int:post_id>", methods=["POST"])
def comment(post_id):

    title = request.form.get("title")
    content = request.form.get("content")

    if not content:
        abort(400)

    db.add_comment(post_id, title, content)

    flash("Comment added!")

    return redirect(url_for("post", post_id=post_id))


@app.route("/tag/<tag>")
def tag(tag):

    posts = db.get_posts()

    filtered = [p for p in posts if tag in (p["tags"] or "")]

    return render_template("tag.html", posts=filtered, tag=tag)


if __name__ == "__main__":
    app.run(debug=True)