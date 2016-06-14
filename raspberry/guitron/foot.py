from socketIO_client import SocketIO
import logging

logging.getLogger('requests').setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG)

with SocketIO('localhost', 8000) as client:
    client.emit("hello")
