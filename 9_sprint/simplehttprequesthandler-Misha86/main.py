import copy
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import re


class ValidateData:
    def __init__(self):
        self._base_data = USERS_LIST
        self._data = None
        self._method = "get"

    def _get_base_valid_keys(self):
        valid_keys = list(self._base_data[0].keys())
        if self._method == "put":
            valid_keys.remove('id')
        return valid_keys

    def _validate_keys(self):
        validated_keys = list(map(lambda k1, k2: k1 == k2, self._get_base_valid_keys(), self._data.keys()))
        return validated_keys if all(validated_keys) else None

    def _check_user_id_exist(self):
        exist_user_id = next((True for user in self._base_data if user["id"] != self._data['id']), False)
        return exist_user_id

    def validate_data(self, data, method="get"):
        self._data = data
        self._method = method
        if self._validate_keys():
            if self._method != "put" and not self._check_user_id_exist():
                self._data = None
            return self._data
        else:
            return None


USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

user_list = copy.deepcopy(USERS_LIST)
validator = ValidateData()


def reset_user_list(*args, **kwargs):
    global USERS_LIST
    USERS_LIST = copy.deepcopy(user_list)
    return 204, None


def get_users(*args):
    body = USERS_LIST
    return 200, body


def user_obj(request, username):
    user = next((user for user in USERS_LIST if user["username"] == username), None)
    if request["method"] == "get":
        return (200, user) if user else (400, {"error": "User not found"})
    else:
        validated_data = validator.validate_data(request["body"], method='put')
        if validated_data and user:
            user.update(validated_data)
            return 200, user
        return (404, {"error": "User not found"}) if not isinstance(user, dict) \
                                                  else (400, {"error": "not valid request data"})


def create_users(request, indent):
    data = request["body"]
    if isinstance(data, list):
        validate_data = [validator.validate_data(d) for d in data]
        valid_data = USERS_LIST + validate_data if all(validate_data) else None
    else:
        validate_data = validator.validate_data(data)
        valid_data = USERS_LIST + list(validate_data) if validate_data else None
    return (201, data) if valid_data else (400, {})


def delete_obj(request, id):
    user = next((user for user in USERS_LIST if user["id"] == int(id)), None)
    return (200, USERS_LIST.remove(user)) if user else (404, {"error": "User not found"})


url_paths = [
    ["/reset", reset_user_list],
    [r"/user", create_users],
    [r"/user/createWithList", create_users],
    [r"/users", get_users],
    [r"/user/(?P<id>\d+)$", delete_obj],
    [r"/user/(?P<username>\w+)$", user_obj],
]


def pars_path(path, url_paths):
    for url in url_paths:
        exist_path = re.fullmatch(url[0], path)
        if exist_path:
            exist_group = exist_path.groups()
            indent = exist_group[0] if exist_group else None
            return path, url[1], indent
    else:
        return None


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    def response_data(self, method="get"):
        try:
            body = self._pars_body()
        except:
            body = None
        path, function, indent = pars_path(self.path, url_paths)
        request = {"method": method, "body": body, "path": path}
        return function(request, indent)

    def do_GET(self):
        self._set_response(*self.response_data(method=self.command.lower()))

    def do_POST(self):
        self._set_response(*self.response_data(method=self.command.lower()))

    def do_PUT(self):
        self._set_response(*self.response_data(method=self.command.lower()))

    def do_DELETE(self):
        self._set_response(*self.response_data(method=self.command.lower()))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
