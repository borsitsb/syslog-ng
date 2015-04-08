#!/usr/bin/python2.7

import socket
import sys
from datetime import datetime

class Server(object):

    def __init__(self, host, port):
        self.log('Starting server ({}:{})...'.format(host, port))
        self.log('Press Ctrl-C to exit!')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.bind((host, port))
            self.sock.listen(1)
            self.log('Listening on port {}'.format(port))

        except:
            self.log('Can not bind, address already in use!', error=True)
            sys.exit(1)

    def log(self, msg, error=False):
        tag = ''
        if error:
            tag = '[ ERROR ]'

        else:
            tag = '[ INFO ]'

        print('{} {}'.format(tag, msg))

    def run(self):
        while True:
            conn, addr = self.sock.accept()
            time = datetime.now().strftime('%H:%M:%S')
            self.log('Connected by <{}:{}> on <{}>'.format(addr[0], addr[1], time))

            while True:
                data = conn.recv(2048)

                if not data:
                    time = datetime.now().strftime('%H:%M:%S')
                    self.log('Disconnected by <{}:{}> on <{}>'.format(addr[0], addr[1], time))
                    break

                data = data.decode('utf-8')
                data = data.split('\n')
                time = datetime.now().strftime('%H:%M:%S')
                for msg in data[:-1]:
                    print('Log message received on <{}>: {}'.format(time, msg))

if __name__ == '__main__':
    server = Server('localhost', 8888)

    try:
        server.run()

    except KeyboardInterrupt:
        server.log('Stopping server...')
