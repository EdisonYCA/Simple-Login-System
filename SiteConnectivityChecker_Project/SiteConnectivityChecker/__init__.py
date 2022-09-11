__version__ = "0.1.0"
from http.client import HTTPConnection
# initializing an instance of HTTPConnection, and requesting only the headers of target website
connection = HTTPConnection("pypi.org", port=80, timeout=10)
connection.request("HEAD", "/")
# storing our response and inspecting headers
response = connection.getresponse()
response.getheaders()
