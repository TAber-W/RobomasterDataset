import os
import json
import re
import jsonpath

json_path = "kk"
save_path = "j2y"
labels_name = []

for root, dirs, files in os.walk(json_path, topdown=False):
    for i in range(len(files)):
        with open(json_path + "/" + files[i], 'r') as f:
            j = json.load(f)
            save = save_path + "/" +files[i].split(".",1)[0] + ".txt"
            f = open(save,'w')
            label = jsonpath.jsonpath(j, '$..label') 
            points = jsonpath.jsonpath(j, '$..points')

            for t in range (len(label)):
                if label[t] == 'NF':

                    f.write('0')
                    f.write(' ')
                    for s in range(len(points[t])):
                        for ss in range (len(points[t][s])):
                            f.write(str(points[t][s][ss])+' ')
                    f.write("\r\n")
                if label[t] == 'RF':
                    f.write('1')
                    f.write(' ')
                    for s in range(len(points[t])):
                        for ss in range (len(points[t][s])):
                            f.write(str(points[t][s][ss])+' ')
                    f.write("\r\n")
            
           





