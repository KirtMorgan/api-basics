import requests

post_code = requests.get('https://api.postcodes.io/postcodes/RM141SW')
# print(post_code.json())
for key in post_code.json()["result"]:
    print(key, post_code.json()['result'][key])
