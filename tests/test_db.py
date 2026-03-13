import db


def test_get_posts():
    posts = db.get_posts()
    assert posts is not None