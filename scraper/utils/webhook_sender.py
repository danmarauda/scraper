```python
import requests
import json

class WebhookSender:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_data(self, data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.webhook_url, headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            raise ValueError(
                'Request to webhook returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )
```