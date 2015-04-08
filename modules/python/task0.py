import socket
import traceback

class LogDestination(object):

    def open(self):
        """Open a connection to the target service"""
        return True

    def close(self):
        """Close the connection to the target service"""
        pass

    def is_opened(self):
        """Check if the connection to the target is able to receive messages"""
        return True

    def init(self):
        """This method is called at initialization time"""
        return True

    def deinit(self):
        """This method is called at deinitialization time"""
        pass

    def send(self, msg):
        """Send a message to the target service

        It should return True to indicate success, False will suspend the
        destination for a period specified by the time-reopen() option."""
        pass


class PythonDestination(LogDestination):

    def init(self):
        print('<<< Python destination - init >>>')
        self.host = 'localhost'
        self.port = 8888
        self.sock = None
        self.connected = False
        return True

    def open(self):
        print('<<< Python destination - open >>>')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.sock.connect((self.host, self.port))
            self.connected = True
            print('<<< Python destination - open successful >>>')
            return True

        except:
            print('<<< Python destination - open failed >>>')
            e = traceback.format_exc()
            print(e)
            self.sock = None
            self.connected = False
            return False

    def close(self):
        print('<<< Python destination - close >>>')
        self.sock.close()
        self.connected = False

    def is_opened(self):
        print('<<< Python destination - is_opened >>>')
        print(self.connected)
        return self.connected

    def send(self, msg):
        print('<<< Python destination - send >>>')

        try:
            data = msg['MESSAGE'] + '\n'
            data = data.encode('utf-8')
            self.sock.sendall(bytes(data))
            return True

        except:
            print("<<< Python destination - sending failed >>>")
            e = traceback.format_exc()
            print(e)
            self.sock = None
            self.connected = False
            return False
