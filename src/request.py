import requests
import pandas as pd
import os

dataset = pd.read_csv('6696.csv')
script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, 'Downloads/images-1/6696')

try:
    os.makedirs(dest_dir)
except OSError:
    pass # already exists



i = 0

for index, row in dataset.iterrows():
	
	i = i + 1

	url = row['url']

	filename = 'image'+ str(i) + ".png"

	path = os.path.join(dest_dir, filename)

	r = requests.get(url, allow_redirects=True)
	open(path, 'wb').write(r.content)