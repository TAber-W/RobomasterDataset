import shutil
import os
import numpy as np


labels_path = "/Users/apple/Desktop/RM_YoloV5_Network/my_data/inside_record_group_1/3_label"
images_path = "/Users/apple/Desktop/RM_YoloV5_Network/my_data/inside_record_group_1/3"
save_path = "/Users/apple/Desktop/RM_YoloV5_Network/my_data/inside_record_group_1/3_image"

images_name = []
labels_name = []

for root, dirs, files in os.walk(labels_path, topdown=False):
    for i in range(len(files)):
        labels_name.append(files[i].split(".",1)[0])

    
for root, dirs, files in os.walk(images_path, topdown=False):
    for i in range(len(files)):
        images_name.append(files[i].split(".",1)[0])


delete_image = []
for i in range(len(labels_name)):
    for j in range(len(images_name)):
        if labels_name[i] == images_name[j]:
            #print("存在",labels_name[i],images_name[j])
            path =images_path + "/" + images_name[j]+".jpg"
            shutil.copy(path,save_path+ "/" + images_name[j]+".jpg")
            
    

