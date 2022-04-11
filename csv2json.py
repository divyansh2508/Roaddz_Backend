import csv,json

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def csv2json(csvFilePath, jsonFilePath=None):
    data = {'raw-data':[]}
    # Open a csv reader called DictReader
    t = ''
    with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            # Convert each row into a dictionary
            # and add it to data
            for rows in csvReader:
                r = rows[None]
                t = {
                    'time' : r[0],
                    'gfx' : r[1],
                    'gfy' : r[2],
                    'gfz' : r[3],
                    'latt' : r[4],
                    'long' : r[5],
                    'speed' : r[6],
                    
                }
                # r --> 8 [time] [gfx] [gfy] [gfz] [Latt] [Long] [Speed] [backchodi]
                # print(t)
                data['raw-data'].append(t)

        # Open a json writer, and use the json.dumps()
        # function to dump data
    if not (jsonFilePath == None):
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
    # print(data)
    return data
            
# Driver Code

csvFilePath = './rawdata/2022-02-2209.02.02full.csv'
# #raw_df=pd.read_csv('./rawdata/2022-02-2209.02.02full.csv')
jsonFilePath = 'ayush.json'

# # Call the make_json function
# jsonobject = csv2json(csvFilePath, jsonFilePath)
# jsonobject = csv2json(csvFilePath)
# print(jsonobject['raw-data'][455]['time'])
if __name__=="__main__":
    import sys