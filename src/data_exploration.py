import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
#navigate to to stored file in Kaggle
for dirname, _, filenames in os.walk('/kaggle/input/google-landmarks-dataset'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


#find top 11 landmarks with most amount of images linked to them
def getlandmark():

	df = pd.read_csv('/kaggle/input/google-landmarks-dataset/train.csv')
	print(df.shape)
	n = 11
	df['landmark_id'].value_counts()[:n].index.tolist()


'''
['9633',
 '6051',
 'None',
 '6599',
 '9779',
 '2061',
 '5554',
 '6651',
 '5376',
 '6696',
 '4352']
 '''