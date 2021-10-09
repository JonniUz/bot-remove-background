import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-host': "background-removal.p.rapidapi.com",
    'x-rapidapi-key': "d6f5c401c9msh7f27cfe69d5f1f9p120948jsn2090fc891893"
}



async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()['response']['image_url']
