### Patched local copy of socketIO-client to work around this issue:
## https://github.com/invisibleroads/socketIO-client/issues/99
#

from socketio_client_local import socketIO_client
import logging

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

with socketIO_client.SocketIO('localhost', 8000) as client:
    client.emit("hello")
