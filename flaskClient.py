import requests


def get_message():
    # Tell request that our CA is legit
    response = requests.get("https://127.0.0.1:5000")
    print(f"Message:{response.content} ")


if __name__ == "__main__":
    get_message()
