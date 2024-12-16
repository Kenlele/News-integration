import logging


class ApiBase:
    def __init__(self, session, url):
        self.url = url
        self.session = session
        self.response = None

    def api_request(self, method, payload=None, data=None, files=None, params=None):
        print(f"Request method: {method}")
        print(f"Request url: {self.url}")
        print(f"payload: {payload}")
        print(f"data: {data}")
        print(f"Request Cookies: {self.session.cookies}")
        print(f"Request headers: {self.session.headers}")
        self.response = self.session.request(method, self.url, json=payload, data=data, files=files, params=params)
        print(f"response.json(): {self.response.json()}")
        self.session.close()
        return self.response.json()
