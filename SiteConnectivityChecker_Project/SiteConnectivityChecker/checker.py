from http.client import HTTPConnection
from urllib.parse import urlparse


def is_online(url, timeout=2):
    """Return true is target URL is online, raise exception otherwise."""
    error = Exception("unknown error")  # defining exception as error
    parser = urlparse(url)  # function that parses target URL
    host = parser.netloc or parser.path.split("/")[0]  # extracting the host name from target url
    for port in (80, 443):  # used to check connection on both HTTP and HTTPS ports
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            # makes a request to target URL, returns true if request is successful
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            # keeps a reference to exception error
            error = e
        finally:
            # closes connection to acquire recourses
            connection.close()
    raise error  # raises exception stored in error if loop finishes without successful request
