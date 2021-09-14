import json
import csv

json_list = []                                          # store the converted json data for each line
csv_file = open("csv_file_name.csv" , "r" )

for line in csv_file.readlines():
    variable1_name, variable2_name, variable3_name = line.strip().split(",")       # first get rid of the \n and then split with ','

    data ={
        "variable1_name" = variable1_name,               #variable name according to your csv file 
        "variable2_name" = variable2_name,
        "variable3_name" = variable3_name
    }
    json_list.append(data)

csv_file.close()

json_file = open("output_json_file_name.json" , "w")              # write json data to a output file
json.dump(json_list, json_file)
json_file.close()
