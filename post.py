import requests

BLOG_URL = "https://api.npoint.io/674f5423f73deab1e9a7"

class Post:
    def __init__(self):
        self.response = requests.get(url=BLOG_URL)
        self.data = self.response.json()
