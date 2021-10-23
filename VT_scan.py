# importing the BeautifulSoup Library
import csv
import os
import time
import requests
import dotenv

dotenv.load_dotenv()

CUSTOM_HEADER = {'x-apikey': os.environ.get('API_KEY')}
VT_URL = 'https://www.virustotal.com/api/v3/search?query='
MY_URL = 'https://raw.githubusercontent.com/ashubits/Threat-Intel-course/main/mdf_files.txt'
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), f'sha_report_{time.strftime("%Y%m%d_%H%M%S")}.csv')

# Creating the requests
response = requests.get(MY_URL)
output_contents = [i.strip() for i in response.text.split('\r')]

with open(OUTPUT_FILE, 'w', newline='') as file:
    # identifying header
    header = ['md5', 'type_description', 'type_extension', 'size',
              'vhash', 'sha256', 'sha1', 'authentihash', 'remarks']
    writer = csv.DictWriter(file, fieldnames=header)

    # writing data row-wise into the csv file
    writer.writeheader()
    for content in output_contents:        
        try:
            time.sleep(15)
            resp = requests.get(f"{VT_URL}{content}", headers=CUSTOM_HEADER)
            data = resp.json()['data'][0]
            writer.writerow({
                'type_description': data["attributes"]["type_description"],
                'type_extension': data["attributes"]["type_extension"],
                'size': data["attributes"]["size"],
                'vhash': data["attributes"]["vhash"],
                'sha256': data["attributes"]["sha256"],
                'sha1': data["attributes"]["sha1"],
                'md5': data["attributes"]["md5"],
                'authentihash': data["attributes"]["authentihash"],
                'remarks': f'https://www.virustotal.com/gui/search/{content}'})
        except Exception as e:
            writer.writerow({                
                'md5': content,            
                'remarks': 'File not found'})
