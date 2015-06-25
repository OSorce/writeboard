#coding=utf8

from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room, \
    close_room, disconnect

def create_socketio(app):
    app.debug = True
    app.config['SECRET_KEY'] = 'secret!'
    socketio = SocketIO(app)

    @socketio.on('subscribe', namespace='/remote')
    def subscribe(message):
        join_room(message['channel'])
        emit('confirm', message, room=message['channel'])

    @socketio.on('publish', namespace='/remote')
    def publish(message):
        emit('slidechanged', message, room=message['channel'])
        emit('confirm', message, room=message['channel'])

    @socketio.on('unsubscribe', namespace='/remote')
    def unsubscribe(message):
        leave_room(message['channel'])

    @socketio.on('connect', namespace='/remote')
    def connect():
        emit('confirm', {'conn': 'conn'})

    @socketio.on('disconnect', namespace='/remote')
    def disconnect():
        pass

    return socketio

if __name__ == '__main__':
    app = Flask(__name__)
    socketio = create_socketio(app)
    socketio.run(app, port=5001)
