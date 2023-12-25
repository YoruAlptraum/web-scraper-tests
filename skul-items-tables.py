import requests
from bs4 import BeautifulSoup
import os

# Replace 'your_website_url' with the actual URL of the website containing the table
url = 'https://skul.fandom.com/wiki/Equipment'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Replace 'your_table_id' with the actual ID of the table containing the images
tables = soup.find_all('table', {'class': 'fandom-table'})

text_path = os.path.join(os.path.expanduser("~"), "Downloads", "tables.txt")

with open(text_path, 'w') as file:
    # Write the text to the file
    for table in tables[1:]:
        file.write('[table]\n')
        for i, row in enumerate(table.find_all('tr')):
            text_row = '[tr]\n'
            if i == 0:
                for data in row.find_all('th'):
                    text_row += '\t[th]'+data.text.strip()+'[/th]\n'
                text_row += '\t[th]'+'Effect'+'[/th]\n'
            else:
                for data in row.find_all('td'):
                    text_row += '\t[td]'+data.text.strip()+'[/td]\n'
            file.write(text_row+'[/tr]\n')
        file.write('[/table]\n')

print('Finished transposing data peko!')
