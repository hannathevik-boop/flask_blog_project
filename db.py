import sqlite3

DATABASE = "database/blog.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def get_posts():
    conn = get_db()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY created DESC"
    ).fetchall()
    conn.close()
    return posts


def get_post(post_id):
    conn = get_db()
    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()
    conn.close()
    return post


def create_post(title, body, tags, image):
    conn = get_db()
    conn.execute(
        "INSERT INTO posts (title, body, tags, image) VALUES (?, ?, ?, ?)",
        (title, body, tags, image),
    )
    conn.commit()
    conn.close()


def update_post(post_id, title, body, tags):
    conn = get_db()
    conn.execute(
        "UPDATE posts SET title=?, body=?, tags=? WHERE id=?",
        (title, body, tags, post_id),
    )
    conn.commit()
    conn.close()


def get_comments(post_id):
    conn = get_db()
    comments = conn.execute(
        "SELECT * FROM comments WHERE post_id=? ORDER BY created DESC",
        (post_id,),
    ).fetchall()
    conn.close()
    return comments


def add_comment(post_id, title, content):
    conn = get_db()
    conn.execute(
        "INSERT INTO comments (post_id, title, content) VALUES (?, ?, ?)",
        (post_id, title, content),
    )
    conn.commit()
    conn.close()
    