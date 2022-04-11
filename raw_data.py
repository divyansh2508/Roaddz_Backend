import geopy.distance, csv, json
def makejson(csvfile, jsonfile):
    data={}
    with open(csvfile, encoding='utf-8') as csvf:
        csvReader=csv.DictReader(csvf)
        for rows in csvReader:
            print(rows)
            key=rows['None']
            data[key] = rows
    with open(jsonfile,'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'./rawdata/2022-02-2209.02.02full.csv'
jsonFilePath = r'sample.json'
 
makejson(csvFilePath, jsonFilePath)
# with open("./rawdata/2022-02-2209.02.02full.csv","r") as x:
#     c = csv.reader(x, delimiter=',', quotechar='|')
    # for row in c:
    #     # print(row)
    #     print(row)
    #print(dir(c))
# distance_point = geopy.distance.geodesic(test_point_vec, test_vec)
# print(distance_point)