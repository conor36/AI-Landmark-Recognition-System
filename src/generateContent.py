import pandas as pd
import os

# This file is to match the building id with an id in a csv file and return a name, description and wiki link 
# relevant to the building.

class BuildingData():


	def getData(self,predictionID):
		print(predictionID)
		dataset = pd.read_csv('Workbook1.csv', encoding= 'unicode_escape')
		
		i = 0
		result = {}
		for index, row in dataset.iterrows():
	
			i = i + 1

			id = row['ID']
			name = row['Name']
			description = row['Description']
			link = row['Link']
			if str(predictionID) == str(id):
				result["Name"] = name
				result["description"] = description
				result["link"] = link

				return (result)


