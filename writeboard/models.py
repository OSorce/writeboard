from datetime import datetime
from werkzeug.security import gen_salt
from flask import current_app, request, url_for
from . import db

class CacheText(db.Model):
    __tablename__ = 'text'
    key = db.Column(db.String(8), primary_key=True)
    text = db.Column(db.Text)

    @classmethod
    def insert_text(cls, text):
        key = gen_salt(8)
        t = CacheText(key=key, text=text)

        try:
            db.session.add(t)
            db.session.commit()
        except:
            db.session.rollback()

        return key
