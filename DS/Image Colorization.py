import requests
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    data={
        'image': 'YOUR_IMAGE_URL',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())


# Example posting a local image file:

import requests
r = requests.post(
    "https://api.deepai.org/api/colorizer",
    files={
        'image': open('LEETCODE/DS/pics/BW1.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())