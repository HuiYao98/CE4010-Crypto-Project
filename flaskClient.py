from certAuthority import *

import requests
from requests_toolbelt.adapters import host_header_ssl


def get_message():
    # response = requests.get("https://google.com")
    # Tell request that our CA is legit"
    s = requests.Session()
    s.mount("https://", host_header_ssl.HostHeaderSSLAdapter())
    r = s.get("https://127.0.0.1:5000", headers={"Host": "localhost"})

    print(r.text)


"""    /*
    response = requests.get(
        "https://127.0.0.1:5000", verify="ca-public-key.pem"
    )"""

# print(f"Message:{response.content} ")


if __name__ == "__main__":
    get_message()
