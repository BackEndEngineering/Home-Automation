import socketio
import logging

serv = socketio.Server()
logger = logging.getLogger(__name__)

@serv.on('connect')
def connect(sid, env):
    logger.error("Connected sid {sid}".format(sid=sid))

@serv.on('hello')
def connect(sid):
    logger.error("Hello msg")
    return 'ok'

@serv.on('disconnect')
def disconnect(sid):
    logger.error("Disconnected sid {sid}".format(sid=sid))
