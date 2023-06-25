import requests

class ConvoxApiClient:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def get_call_status(self, call_id):
        url = f"{self.api_url}/calls/{call_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_call_history(self):
        url = f"{self.api_url}/calls"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(url, headers=headers)
        return response.json()

    def make_call(self, phone_number):
        url = f"{self.api_url}/calls"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        data = {"phone_number": phone_number}
        response = requests.post(url, headers=headers, json=data)
        return response.json()
