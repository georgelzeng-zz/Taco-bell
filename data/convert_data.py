# convert nutrition data csv into json list

import json
import csv

FILE = "nutrition.csv"

reader = csv.reader(open(FILE))

# skip header
next(reader)

# create json list
menu = []
for item in reader:
	item_data = {}
	item_data["name"] = item[0]
	item_data["p"] = item[1]
	item_data["c"] = item[2]
	item_data["f"] = item[4] 
	menu.append(item_data)

# sort list
price_sort = sorted(menu, key=lambda k: k['p'])

# write json file
json_list = json.dumps(price_sort, ensure_ascii=False)
new_file = "nutrition.json"
file = open("nutrition.json", "w")
file.write(json_list)


# import csv
# import pprint

# FILE = "nutrition.csv"

# reader = csv.DictReader(open(FILE, 'rb'))

# menu = []
# for item in reader:
# 	menu.append(item)

# #sort list
# price_sort = sorted(menu, key=lambda k: k['Price'])
# pprint.pprint(price_sort)



