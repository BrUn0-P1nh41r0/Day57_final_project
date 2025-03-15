import requests

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

class Post:
    def __init__(self):
        self.response = requests.get(url=BLOG_URL)
        self.data = self.response.json()
