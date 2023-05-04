import requests

url = "https://github.com/djordjepetrovicHTEC/Script-for-README-automation"

headers = {
    "Authorization": "Bearer test",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # process the response data
else:
    # handle error cases
