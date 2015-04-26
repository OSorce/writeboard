#!/usr/bin/env python
import os

from writeboard import create_app, db
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from writeboard.models import CacheText

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def init():
    " Init Database. "
    db.create_all()


@manager.command
def data():
    " Get all data from db."
    d = CacheText.query.all()
    for _d in d:
        print(_d.text)


if __name__ == '__main__':
    manager.run()
