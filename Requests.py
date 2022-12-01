import json

import requests

post_data = {"id": 10001,
             "category": {"id": 1, "name": "dog"},
             "name": "dog 1",
             "photoUrls": ['string'],
             "tags": [{"id": 1, "name": "string"}],
             "status": "available"}
put_data = {"id": 10001,
            "category": {"id": 1, "name": "dog"},
            "name": "DOG 1",
            "photoUrls": ['string'],
            "tags": [{"id": 1, "name": "string"}],
            "status": "available"}
base_url = "https://petstore.swagger.io/v2/"
get_url = f"pet/{post_data.get('id')}"
post_url = "pet"
put_url = "pet"
delete_url = f"pet/{post_data.get('id')}"

post_data = json.dumps(post_data)
put_data = json.dumps(put_data)
post_response = requests.post(f"{base_url}" + f"{post_url}", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=post_data)
print(post_response.text)
get_response = requests.get(f"{base_url}" + f"{get_url}", params={'status': 'available'}, headers={'accept': 'application/json'})
print(get_response.text)
put_response = requests.put(f"{base_url}" + f"{put_url}", headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=put_data)
print(put_response.text)
delete_response = requests.delete(f"{base_url}" + f"{delete_url}", headers={'accept': 'application/json'})
print(delete_response.text)
