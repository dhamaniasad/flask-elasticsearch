from app import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'Post'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    created_time = db.Column(db.DateTime())

    def __init__(self, title, text, created_time=None):
        self.title = title
        self.text = text
        if created_time is None:
            self.created_time = datetime.utcnow()
        else:
            self.created_time = created_time


class Comment(db.Model):
    __tablename__ = 'Comment'
    comment_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text())
    author = db.Column(db.Text())
    created_time = db.Column(db.DateTime())
    post_id = db.Column(db.Integer, db.ForeignKey('Post.post_id'))
    post = db.relationship('Post',
            backref=db.backref(
                'comments', 
                lazy='dynamic', 
                cascade='all,delete-orphan'
                )
            )

    def __init__(self, post_id, author, text, created_time=None):
        self.post_id = post_id
        self.author = author
        self.text = text
        if created_time is None:
            self.created_time = datetime.utcnow()
        else:
            self.created_time = created_time
