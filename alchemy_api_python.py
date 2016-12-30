import json
import csv
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='7b82d560ee3d0affc71e93770dca3a6349e7e386')


def csvdata_to_list(data):
    d=[]
    for row in data:
        d.append(row)
    return d

def write_list_in_file(final, name):
    with open(name, "w", newline="",encoding="utf8") as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(final)

d1 = csv.reader(open('status_80percent_eng.csv', 'r', encoding="utf8"))
d1 = csvdata_to_list(d1)
data ={"index": []}
for i in range(940,1190):
	#print( d1[i][1])
	
	try:
		response = alchemy_language.combined(text=d1[i][1],extract='keywords,concepts,doc-sentiment,doc-emotion',sentiment=1,max_items=1)		
		data["index"].append(response)
		print("done!")
	
	except Exception as e: 
		print("cant decode it. Exception: "+ str(e) )

	
	

with open('data4.json', 'w') as outfile:
	json.dump(data, outfile)



