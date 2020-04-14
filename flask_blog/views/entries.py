from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app, db
from flask_blog.models.entries import Entry
from flask_blog.views.views import login_required

@app.route('/')
@login_required
def show_entries():
    entries = Entry.query.order_by(Entry.post_id.desc()).all()
    return render_template('entries/index.html', entries=entries)

@app.route('/entries/new', methods=['GET'])
@login_required
def new_entry():
    return render_template('entries/new.html')

@app.route('/entries', methods=['POST'])
@login_required
def add_entry():
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:post_id>', methods=['GET'])
@login_required
def show_entry(post_id):
    entry = Entry.query.get(post_id)
    return render_template('entries/show.html', entry=entry)

@app.route('/entries/<int:post_id>/edit', methods=['GET'])
@login_required
def edit_entry(post_id):
    entry = Entry.query.get(post_id)
    return render_template('entries/edit.html', entry=entry)

@app.route('/entries/<int:post_id>/update', methods=['POST'])
@login_required
def update_entry(post_id):
    entry = Entry.query.get(post_id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))


@app.route('/entries/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_entry(post_id):
    entry = Entry.query.get(post_id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))