from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app, make_response, jsonify
from flask.ext.sqlalchemy import get_debug_queries
from . import main
from .. import db
from ..models import CacheText
from .forms import WritesForm


@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/write', methods=['GET', 'POST'])
@main.route('/write/<key>', methods=['GET', 'POST'])
def write(key=None):
    form = WritesForm()
    if request.method == 'GET':
        if key:
            content = CacheText.query.get(key)
            if content:
                form.text.data = content.text
                form.key.data = content.key
        return render_template('main/write.html', form=form)
    else:
        if form.validate_on_submit():
            text = form.text.data
            if not key:
                key = CacheText.insert_text(text)
            else:
                t = CacheText.query.get(key)
                if t:
                    t.text = text
                    db.session.add(t)
                    db.session.commit()
                else:
                    abort(404)
            return jsonify(status='ok', key=key)
        return jsonify(status='err', errors=form.errors)


@main.route('/posts', methods=['GET', 'POST'])
@main.route('/posts/<key>', methods=['GET', 'POST'])
def posts(key=None):
    if request.method == 'GET':
        if key:
            content = CacheText.query.get(key)
            if content:
                return render_template('main/post.html', texts=content.text)
    else:
        text = request.form.get('text')
        if text:
            return render_template('main/post.html', texts=content.text)
    return redirect(url_for('write'))


@main.route('/slide', methods=['GET', 'POST'])
@main.route('/slide/<key>', methods=['GET', 'POST'])
def slide(key=None):
    slide = {'key': key}
    form = WritesForm()
    if request.method == 'GET':
        if request.args.get('remote'):
            slide['master'] = True
        if key:
            content = CacheText.query.get(key)
            if content:
                pages = content.text.split('\n---\n')
                return render_template('main/slide.html', texts=pages, slide=slide)
    else:
        text = request.form.get('text')
        pages = text.split('\n---\n')
        if text:
            return render_template('main/slide.html', texts=pages, slide=slide)
    return redirect(url_for('write'))
