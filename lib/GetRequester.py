import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        return requests.get('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').content

    def load_json(self):
        return json.loads(self.get_response_body())