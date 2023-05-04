import requests

url = "https://api.github.com/repos/USERNAME/REPO"

headers = {
    "Authorization": "Bearer test",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # process the response data
else:
    # handle error cases
