import requests

class xrequest(object):
    def __init__(self):
        super(xrequest, self).__init__()

        self.requests = requests

    def log(self, value, color='[G1]', type=1):
        self.liblog.log(value, color=color, type=type)

    def log_tab(self, value, value_tab, color='[G1]', type=1):
        self.liblog.log_tab(value, value_tab, color=color, type=type)

    def log_replace(self, value, color='[G1]'):
        self.liblog.log_replace(value, color=color)

    def session(self):
        self.requests = requests.Session()

        return self

    def quote(self, value, safe=None):
        return requests.utils.quote(value, safe=safe)

    def request(self, method, target, headers={}, data=None, json=None, timeout=30):
        while True:
            try:
                return self.requests.request(method, target, headers=headers, data=data, json=json, timeout=timeout)

            except requests.exceptions.Timeout:
                self.log_tab('Connection Timeout:', [target, 'sleep 3 seconds.'], color='[R1]')
                self.liblog.sleep(3)

            except requests.exceptions.ConnectionError:
                self.log_tab('No Connection:', [target, 'sleep 10 seconds.'], color='[R1]')
                self.liblog.sleep(10)

            except KeyboardInterrupt:
                raise KeyboardInterrupt
