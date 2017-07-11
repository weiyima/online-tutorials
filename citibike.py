# source: https://www.youtube.com/watch?v=Dm-o10JPGis&list=PLehYFEvQGUkGVNatdOfuSqOQLRCCI9SYH
# import urllib.request, urllib.parse, urllib.error
import json
import csv
import glob

outputFile = open("convertedJSON.csv","w")
outputWriter = csv.writer(outputFile)

# fname = 'citibike_data.json'

needs_header = True

folder_name = 'json_downloads'
for fname in glob.iglob(folder_name+"/*.json"):
    
    sourceFile = open(fname, "rU") # Open the file containing the JSON data
    json_data = json.load(sourceFile) #Load file into json library. Returns dictionary
    # print(json_data)
    # exec_time = json_data["executionTime"]
    # print(exec_time)

    # stationBeanList = json_data["stationBeanList"] # this is a list of dicts.
    for station in json_data["stationBeanList"] :
        
        # Add 1 row of headers, set header flag to False 
        if needs_header == True :
            header_row = []
            header_row.append("file_date")
            for attribute in station :
                header_row.append(attribute) # attribute is a string
            outputWriter.writerow(header_row)
            needs_header = False

        # Appends time, then unique value for each attribute
        row_list = []
        row_list.append(json_data["executionTime"])
        
        for attribute in station :
            row_list.append(station[attribute])
        outputWriter.writerow(row_list)

sourceFile.close()
outputFile.close()