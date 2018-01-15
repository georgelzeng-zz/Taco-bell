import argparse
import json
import ast
import pprint


def knapsack(menu, cost, fat):
	rows = fat
	cols = cost
	dp = [([{}] * rows) for col in range(cols)]

	o_n = 0
	o_f = 0

	for row in range(rows):
		dp[0][row][0] = []
	for col in range(cols):
		dp[col][0] = {0 : []}


	for col in range(1, cols):
		for row in range(1, rows):
			if not dp[col][row]:
				purchase = []
				nutrition = -1
				for item in menu:
					if col - int(item['p']) < 0 or row - int(item['f']) < 0:
						continue
					pre_location = dp[col - int(item['p'])][row - int(item['f'])]
					if pre_location.keys()[0] + int(item['c']) > nutrition:
						nutrition = pre_location.keys()[0] + int(item['c'])
						purchase = pre_location.values()[0] + [item['name']]
						if nutrition > o_n:
							o_n = nutrition
							o_f = row + 1
				if nutrition < dp[col - 1][row].keys()[0]:
					nutrition = dp[col - 1][row].keys()[0]
					purchase = dp[col - 1][row].values()[0]	
				if nutrition < dp[col][row - 1].keys()[0]:
					nutrition = dp[col][row - 1].keys()[0]
					purchase = dp[col][row - 1].values()[0]
				if nutrition < dp[col - 1][row - 1].keys()[0]:
					nutrition = dp[col - 1][row - 1].keys()[0]
					purchase = dp[col - 1][row - 1].values()[0]
			dp[col][row] = {nutrition : purchase}
	
	return sorted(dp[cols - 1][rows - 1].values()[0]), o_n, o_f



if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("cost", help = "total money", type=int)
    parser.add_argument("fat", help = "fat limit", type=int)
    args = parser.parse_args()

    json_file = open('nutrition.json')
    json_str = json_file.read()
    json_data = ast.literal_eval(json_str)
print knapsack(json_data, args.cost, args.fat)

