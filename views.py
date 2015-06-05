from app import app, db
from flask import render_template, request, url_for, redirect
from forms import CreateForm, CommentForm
from models import Post, Comment


@app.route('/')
def homepage():
    posts = Post.query.all()
    return render_template('list.html', posts=posts)


@app.route('/create', methods=['GET'])
def create():
    my_form = CreateForm(csrf_enabled=False)
    return render_template('create.html', form=my_form)


@app.route('/<int:post_id>', methods=['GET'])
def view(post_id):
    comment_form = CommentForm(csrf_enabled=False)
    found_post = Post.query.get(post_id)
    return render_template('view.html', post=found_post, comment_form=comment_form)


@app.route('/<int:post_id>/edit', methods=['GET'])
def edit_post(post_id):
    found_post = Post.query.get(post_id)
    my_form = CreateForm(obj=found_post, csrf_enabled=False)
    return render_template('create.html', form=my_form)


@app.route('/save', methods=['POST'])
def save():
    my_form = CreateForm(csrf_enabled=False)
    my_post = None
    if not my_form.post_id.data and my_form.validate_on_submit():
        my_post = Post(my_form.title.data, my_form.text.data)
        db.session.add(my_post)
    if my_form.post_id.data and my_form.validate_on_submit():
        my_post = Post.query.get(my_form.post_id.data)
        my_post.title = my_form.title.data
        my_post.text = my_form.text.data
    db.session.commit()
    return redirect(url_for('view', post_id=my_post.post_id))


@app.route('/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    found_post = Post.query.get(post_id)
    db.session.delete(found_post)
    db.session.commit()
    return redirect(url_for('homepage'))


@app.route('/<int:post_id>/comments', methods=['POST'])
def add_comment(post_id):
    comment_form = CommentForm(csrf_enabled=False)
    if comment_form.validate_on_submit():
        c_comment = Comment(
                comment_form.post_id.data,
                comment_form.author.data,
                comment_form.text.data)
        db.session.add(c_comment)
        db.session.commit()
    return redirect(url_for('view',post_id=post_id))

