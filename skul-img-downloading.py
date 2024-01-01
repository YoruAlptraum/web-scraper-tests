import requests
from bs4 import BeautifulSoup
import os
import urllib
import re

# Replace 'your_website_url' with the actual URL of the website containing the table
url = 'https://skul.fandom.com/wiki/Equipment'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Replace 'your_table_id' with the actual ID of the table containing the images
tables = soup.find_all('table', {'class': 'fandom-table'})

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
directory_path = os.path.join(downloads_path, "skul_icons")
# Create a folder to store the downloaded images
os.makedirs(directory_path, exist_ok=True)

# Iterate through the table rows
for table in tables[1:]:
    for image in table.find_all('a', {'class':'image'}):        
        if not (image_src:= image.find('img').get('data-src')):
            image_src = image.find('img').get('src')
                
        img_title = image.find_next_sibling().get('title')
        print(img_title)

        image_name = re.sub(r'[^a-zA-Z0-9]', '', img_title) + '.png'
        # Download the image
        # print(os.path.join(directory_path, image_name))
        urllib.request.urlretrieve(image_src, os.path.join(directory_path, image_name))


print("Images finished downloading peko!")


