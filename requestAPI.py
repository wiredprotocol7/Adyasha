import requests
from requests.exceptions import HTTPError
import re


def replace(word):
    if "{" in word:
        word = word.split("{")
        return word[0]
    return word


base_url = "http://api.zooinverse.com/v2"

# GET Requests to the api endpoints


music_GET_API_endpoints = ["SearchbyContId/{contentId}", "/music/SearchbyUserId/{userId}", "SearchbySimilarUser/{userId}",
                           "SearchbySimilarContId/{contentId}","/music/SearchbyMetadata"]

for endpoints in music_GET_API_endpoints:
    url = base_url + "/music/" + endpoints
    try:
        url = replace(url)
    except:
        continue
    if "{" in endpoints:
        id = input("Enter the Id.")
        url += id
    try:
        response=requests.get(url)
        response.raise_for_status()

    except HTTPError as http_err:
     print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        print(response)

video_GET_API_endpoints=["viewThumbnail/{videoID}"]
for endpoints in video_GET_API_endpoints:
    url = base_url + "/video/" + endpoints
    try:
        url = replace(url)
    except:
        continue
    if "{" in endpoints:
        id = input("Enter the Id.")
        url += id
    try:
        response=requests.get(url)
        response.raise_for_status()

    except HTTPError as http_err:
     print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        print(response)
video_POST_API_endpoints=["uploadVideo"]
for endpoints in video_GET_API_endpoints:
    url = base_url + "/video/" + endpoints
    try:
        url = replace(url)
    except:
        continue
    if "{" in endpoints:
        id = input("Enter the Id.")
    try:
        data = {'metada': "MetadataSample",
                'filename': "Samplevideo.mp4"}
        response=requests.post(url,data=data)
        response.raise_for_status()

    except HTTPError as http_err:
     print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!')
        print(response)
