import os
import json
import re
import jsonpath

json_path = "kk"
save_path = "j2y"
labels_name = []
yy=[]
xx=[]

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
                            if ss == 0:
                                #f.write(str(points[t][s][ss]/1280)+' ')
                                xx.append(points[t][s][ss]/1280)
                            elif ss == 1:
                                #f.write(str(points[t][s][ss]/1024)+' ')
                                yy.append(points[t][s][ss]/1024)
                    xmax = max(xx)
                    xmin = min(xx)
                    ymax = max(yy)
                    ymin = min(yy)
                    xcenter = (xmax+xmin)/2
                    ycenter = (ymax+ymin)/2
                    w = xmax - xmin
                    h = ymax - ymin
                    f.write(str(round(xcenter,6)) + " " + str(round(ycenter,6)) + " " + str(round(w,6)) + " " + str(round(h,6))+" ")
                    for aa in range(5):
                        f.write(str(xx[aa])+" ")
                        f.write(str(yy[aa])+" ")
                    xx = []
                    yy = []
                    f.write("\r\n")
                if label[t] == 'RF':
                    f.write('1')
                    f.write(' ')
                    for s in range(len(points[t])):
                        for ss in range (len(points[t][s])):
                            if ss == 0:
                                #f.write(str(points[t][s][ss]/1280)+' ')
                                xx.append(points[t][s][ss]/1280)
                            elif ss == 1:
                                #f.write(str(points[t][s][ss]/1020)+' ')
                                yy.append(points[t][s][ss]/1024)
                    xmax = max(xx)
                    xmin = min(xx)
                    ymax = max(yy)
                    ymin = min(yy)
                    xcenter = (xmax+xmin)/2
                    ycenter = (ymax+ymin)/2
                    w = xmax - xmin
                    h = ymax - ymin
                    f.write(str(round(xcenter,6)) + " " + str(round(ycenter,6)) + " " + str(round(w,6)) + " " + str(round(h,6))+" ")
                    for aa in range(5):
                        f.write(str(xx[aa])+" ")
                        f.write(str(yy[aa])+" ")
                    xx = []
                    yy = []
                    f.write("\r\n")
            
           





