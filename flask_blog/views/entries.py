from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app, db
from flask_blog.models.entries import Entry

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.order_by(Entry.post_id.desc()).all()
    return render_template('entries/index.html', entries=entries)

@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')

@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry(
        title = request.form['title'],
        text = request.form['text']
    )
    db.session.add(entry)
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:post_id>', methods=['GET'])
def show_entry(post_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(post_id)
    return render_template('entries/show.html', entry=entry)

@app.route('/entries/<int:post_id>/edit', methods=['GET'])
def edit_entry(post_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(post_id)
    return render_template('entries/edit.html', entry=entry)

@app.route('/entries/<int:post_id>/update', methods=['POST'])
def update_entry(post_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(post_id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))


@app.route('/entries/<int:post_id>/delete', methods=['POST'])
def delete_entry(post_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(post_id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました')
    return redirect(url_for('show_entries'))